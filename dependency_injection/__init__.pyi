from typing import Type


def service(cls: Type) -> Type:
    """
    Decorate for classes. Classes decorated with @service will be registered into the service container. No 2 services
    can have the same key nor value. The __init__ member of classes decorated with @service will be injected with
    defined services from the container during initialization.
    :param cls:
    :return:
    """
    ...

def client(cls: Type) -> Type:
    """
    Decorator for classes. Classes decorated with @client will have their __init__ member injected with services from
    the container during initialization.
    :param cls: Class
    :return: Class
    """
    ...

def register_service(**kwargs) -> None:
    """
    Registers a single (key, value) pair as a variable service. No 2 services can have the same key nor value.
    It is recommended to use the alias "register_services" for multiple (key, value) pairs.
    :param kwargs: variable name and value pair to register
    :return: None
    """
    ...

def register_services(**kwargs) -> None:
    """
    Registers multiple (key, value) pairs as a variable service. No 2 services can have the same key nor value. It is
    recommended to use the alias "register_service" for a single (key, value) pair.
    :param kwargs: variable name and value pairs to register
    :return: None
    """
    ...
