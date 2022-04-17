# Dependency Injection

This library supports dependency injection into the constructor of any class.
Dependency Injection should be implemented ONLY in libraries using the OOP paradigm.

## Annotations

For simplicity, are 2 main annotations to be aware of:

### `@service`

Used on classes which should be registered into a container.
If any params are defined in the __init__ method, they should be registered in the IoC.

### `@client`

Used to inject services into classes using the constructor.

### Use Case

```python
# import the service annotation
from dependency_injection import service, client


# register MyService class into the IoC container
@service
class MyService:
    pass


# register MyServiceWithParams into the IoC container.
@service
class MyServiceWithParams:
    
    # MyService is automatically injected into the constructor.
    # This would not be possible if MyService was not registered
    def __init__(self, my_service: MyService):
        self.my_service = my_service

       
# specifies MyClient is calling services from IoC container using `typing` annotations
@client
class MyClient:
    
    def __init__(
        self,
        my_service: MyService,  # --> refers to the MyService registered in IoC
        my_service_with_params: MyServiceWithParams  # --> refers to MyServiceWithParams
    ):
        self.my_service = my_service
        self.my_service_with_params = my_service_with_params
```

### Registering variables using `register_service()`

Alternatively, you can use the `register_service()` function to register services.
With this approach, you can must specify a param name on which to register the service.

NOTE: While you can register classes using this method, it is not recommended.

### Intended Use Case #1
```python
from dependency_injection import client, register_service

register_service(api_key='123-456-7890')


@client
class MyClient
    
    def __init__(self, api_key):
        self.api_key = api_key
```

### Intended Use Case #2
```python
from dependency_injection import client, register_services

register_services(
    api_key='123-456-7890',
    another_api_key='abc-def-ghij'
)
```

## TODO

Allow for sub containers to limit the scope? IE: Global Container, HTTP Container, ETC.


