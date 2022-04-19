from .container import Container as _Container
from .decorators import client, service

register_service = _Container.register_variable_service
register_services = _Container.register_variable_service
