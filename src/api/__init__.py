from .auth import AuthApiClient
from .users import UsersApiClient

def create_api_client(client_type: str, env: str = 'dev'):
    """Фабрика для создания API клиентов"""
    clients = {
        'auth': AuthApiClient,
        'users': UsersApiClient
    }
    return clients[client_type](env=env)
