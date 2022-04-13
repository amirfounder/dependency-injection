from typing import Type, Dict, Any, Optional, Protocol
import builtins


class ContainerService(Protocol):
    def get(self) -> Any: ...


class ContainerClassService(ContainerService):
    def __init__(self, klass: Type):
        self.klass = klass
        self.instance: Any = None

    def get(self):
        if not self.instance:
            self.instance = self.klass()
        return self.instance


class ContainerVariableService(ContainerService):
    def __init__(self, value):
        self.value = value

    def get(self):
        return self.value


class Container(object):
    services: Dict[Type | str, ContainerService] = {}

    @classmethod
    def validate_unique_key(cls, key: str | Type):
        if key in cls.services:
            raise Exception(f'Key already registered: {key}')

    @classmethod
    def register_class_service(cls, klass: Type, name: Optional[str] = None) -> None:
        key = name if name else klass

        cls.validate_unique_key(key)
        cls.services[key] = ContainerClassService(klass)

    @classmethod
    def register_variable_service(cls, name: str, value: Any) -> None:
        cls.validate_unique_key(name)
        cls.services[name] = ContainerVariableService(value)

    @classmethod
    def get_service(cls, name: str, klass: Type):
        key = klass if not hasattr(builtins, klass.__name__) and klass in cls.services else name
        return cls.services.get(key).get()
