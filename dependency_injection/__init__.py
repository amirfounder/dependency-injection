from .container import Container as _Container

from .service import service
from .client import client
register_service = _Container.register_variable_service
