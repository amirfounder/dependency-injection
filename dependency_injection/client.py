from typing import Type

from dependency_injection.injector import Injector


def client(klass: Type):
    Injector.inject_services(klass)
    return klass
