from __future__ import annotations
from dependency_injection import client, service, register_service, register_services


register_service(api_key='ENCRYPTED_VALUE')
register_services(
    number_map={'zero': 0, 'one': 1, 'two': 2, 'three': 3},
    number_list=['zero', 'one', 'two', 'three']
)


@service
class Service1:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def do_something(self):
        pass


@service
class Service2:
    def __init__(self, service1: Service1):
        self.service1 = service1

    def do_something_2(self):
        pass


@client
class Client1:
    def __init__(self, service1: Service1, service2: Service2):
        self.service1 = service1
        self.service2 = service2


@client
class Client2:
    def __init__(self, service1: Service1, service2: Service2):
        self.service1 = service1
        self.service2 = service2


def test_example1():
    client1 = Client1()
    client2 = Client2()

    client1.service1.do_something()
    client2.service1.do_something()

    assert client1.service1 is client2.service1
    assert client1.service1 == client2.service1



