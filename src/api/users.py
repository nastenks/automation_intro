from .client import ApiClient

class UsersApiClient(ApiClient):
    def get_current_user(self) -> dict:
        """Получение данных текущего пользователя"""
        return self._request('GET', '/api/v3/users/me')
    
    def get_user_full_name(self) -> str:
        """Получение полного имени пользователя"""
        user_data = self.get_current_user()
        return user_data.get('data', {}).get('username', {}).get('full', '')