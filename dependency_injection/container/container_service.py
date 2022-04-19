from asyncio import Protocol
from typing import Any, Type


class RegisteredService(Protocol):
    """
    Protocol for all registered services
    """
    def get(self) -> Any: ...


class RegisteredClassService(RegisteredService):
    """
    RegisteredService abstraction for class-based services
    """
    def __init__(self, klass: Type):
        self.klass = klass
        self.instance: Any = None

    def get(self) -> Any:
        """
        Gets the instance of the class service. Will initialize if it has not been already
        :return: Any
        """
        if not self.instance:
            self.instance = self.klass()
        return self.instance


class RegisteredVariableService(RegisteredService):
    """
    RegisteredService abstraction for variable based services
    """
    def __init__(self, value):
        self.value = value

    def get(self) -> Any:
        """
        Gets the value of the service
        :return: Any
        """
        return self.value
