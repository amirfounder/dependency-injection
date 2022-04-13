from dependency_injection.container import Container
from dependency_injection.injector import Injector

from inspect import signature
from typing import Type


def _klass_service():
    pass


def _func_service():
    pass


def service(klass: Type[object]):
    Injector.inject_services(klass)
    Container.register_class_service(klass)

    return klass
