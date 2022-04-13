from .container import Container as _Container

from .service import service
from .client import client

register_service = _Container.register_variable_service
"""
Allows the registration of a singular variable service.
Example::
    register_service(a=1)
Alternatively, registration of multiple variable services is possible, but not recommended.
For registration of multiple variables use::
register_services(...)
"""
register_services = _Container.register_variable_service
