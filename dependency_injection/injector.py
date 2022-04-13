from typing import Type
from inspect import get_annotations

from dependency_injection.container import Container


class Injector:

    @classmethod
    def inject_services(cls, klass: Type):
        init = klass.__init__
        init_signature = get_annotations(init, eval_str=True)

        def new_init(self, *args, **kwargs):
            for name, annotation in init_signature.items():
                if name == 'return':
                    continue
                if _service := Container.get_service(name, annotation):
                    kwargs[name] = _service

            init(self, *args, **kwargs)

        klass.__init__ = new_init
