from .client import ApiClient

class AuthApiClient(ApiClient):
    def login(self, email: str, password: str) -> str:
        """Авторизация и получение токена"""
        data = {
            'email': email,
            'password': password
        }
        response = self._request('POST', '/api/v3/auth/login', json=data)
        self._token = response.get('data', {}).get('token')
        return self._token