import os
import requests
from dotenv import load_dotenv
from typing import Dict, Any


load_dotenv()

class ApiClient:
    def __init__(self, env: str = 'dev'):
        self.base_url = os.getenv(f"{env.upper()}_API_URL")
        self._token = None
        
    def _get_headers(self) -> Dict[str, str]:
        """Базовые заголовки для всех запросов"""
        headers = {
            'Content-Type': 'application/json',
            'x-device-uid': os.getenv("X_DEVICE_UID"),
            'Cookie': 'preferred_language=en'
        }
        if self._token:
            headers['Authorization'] = f'Bearer {self._token}'
        return headers
    
    def _request(self, method: str, endpoint: str, **kwargs) -> Dict[str, Any]:
        """Базовый метод для запросов"""
        url = f"{self.base_url}{endpoint}"
        response = requests.request(
            method=method,
            url=url,
            headers=self._get_headers(),
            **kwargs
        )
        response.raise_for_status()
        return response.json()



class ApiClient:
    def __init__(self, env: str = 'dev'):
        self._token_cache = Path(f".token_{env}.json")
        self._load_token()
        
    def _load_token(self):
        if self._token_cache.exists():
            with open(self._token_cache) as f:
                self._token = json.load(f).get('token')
    
    def _save_token(self):
        with open(self._token_cache, 'w') as f:
            json.dump({'token': self._token}, f)