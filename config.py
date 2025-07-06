# загрузка настроек из переменных окружения
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DEV_URL = os.getenv('DEV_URL')
    STAGE_URL = os.getenv('STAGE_URL')
    PROD_URL = os.getenv('PROD_URL')
    DEV_USER = os.getenv('DEV_USER')
    DEV_PASSWORD = os.getenv('DEV_PASSWORD')
    
    @classmethod
    def get_env_url(cls, env='dev'):
        env = env.lower()
        if env == 'dev':
            return cls.DEV_URL
        elif env == 'stage':
            return cls.STAGE_URL
        elif env == 'prod':
            return cls.PROD_URL
        else:
            raise ValueError(f"Unknown environment: {env}")