from typing import Type, Dict, Optional, Any
import builtins


from dependency_injection.container_service import (
    RegisteredService,
    RegisteredClassService,
    RegisteredVariableService
)


class Container(object):
    """
    The container that holds services and their instance counterparts.
    """
    _services: Dict[Type | str, RegisteredService] = {}

    @classmethod
    def _validate_unique_key(cls, key: str | Type) -> None:
        """
        Checks to see if something is registered under this key. Raises Exception if check fails.
        :param key: The key to check against.
        :return: None
        """
        if key in cls._services:
            raise Exception(f'Key already registered: {key}')

    @classmethod
    def register_class_service(cls, klass: Type, name: Optional[str] = None) -> None:
        """
        Registers the class if the identifier is unique. Raises Exception if identifier is not unique.
        :param klass: The class to register. Used as the identifier if name is not present.
        :param name: Optional parameter to use as identifier.
        :return: None
        """
        key = name if name else klass

        cls._validate_unique_key(key)
        cls._services[key] = RegisteredClassService(klass)

    @classmethod
    def register_variable_service(cls, **kwargs) -> None:
        """
        Validates uniqueness and registers key, value for every key, value provided. Raises Exception if identifier is
        not unique.
        :param kwargs: Keyword arguments.
        :return: None
        """
        for key, value in kwargs.items():
            cls._validate_unique_key(key)
            cls._services[key] = RegisteredVariableService(value)

    @classmethod
    def _get_service_by_class(cls, klass: Type) -> RegisteredService | None:
        """
        Gets service by class if class is not a builtin
        :param klass: The class to get service by.
        :return: ContainerService or None.
        """
        if not hasattr(builtins, klass.__name__):
            return cls._services.get(klass)

    @classmethod
    def _get_service_by_name(cls, name: str) -> RegisteredService | None:
        """
        Gets service by name
        :param name: The name to get service by.
        :return: ContainerService or None.
        """
        return cls._services.get(name)

    @classmethod
    def get_service(cls, name: str, klass: Type) -> Any:
        """
        Retrieves a service's instance by class or name. Searches by class first if class. If class is not a builtin
        and is registered, will try to retrieve service by name. If searching by class nor name return a service, an
        Exception is thrown.
        :param name: The name to retrieve service by.
        :param klass: The class to retrieve service by.
        :return: Any
        """
        if service := cls._get_service_by_class(klass):
            return service.get()
        if service := cls._get_service_by_name(name):
            return service.get()
        raise Exception(f'No service registered under name : {name} or class {klass}')
