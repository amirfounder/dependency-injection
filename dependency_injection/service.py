from dependency_injection.container import Container
from dependency_injection.injector import Injector

from typing import Type


def service(klass: Type[object]):
    Injector.inject_services(klass)
    Container.register_class_service(klass)

    return klass
