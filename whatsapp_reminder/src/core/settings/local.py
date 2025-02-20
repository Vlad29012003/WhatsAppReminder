from .base import *
from pathlib import Path
from decouple import config as env

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')
ALLOWED_HOST = env('ALLOWED_HOSTS',default='*').split(',')
WATI_BASE_URL = env('WATI_BASE_URL', '')
WATI_ACCESS_TOKEN = env('ACCESS_WHATSAPP_TOKEN', '')

print(f"WATI_BASE_URL from env: {env('API_WTATSAPP_Endpoint', '')}")




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('POSTGRES_DB'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': env('POSTGRES_HOST' , default ='localhost'),
        'PORT': env('POSTGRES_PORT' ,default ='5432' ,cast=int)
    }
}