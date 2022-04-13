from typing import Type
from inspect import signature, get_annotations

from dependency_injection.container import Container


class Injector:

    @classmethod
    def inject_services(cls, klass: Type):
        init = klass.__init__
        init_signature = signature(init, eval_str=True)

        def new_init(self, *args, **kwargs):
            for name, param in dict(init_signature.parameters).items():
                if name in ['self', 'return']:
                    continue
                if _service := Container.get_service(name, param.annotation):
                    kwargs[name] = _service

            init(self, *args, **kwargs)

        klass.__init__ = new_init
