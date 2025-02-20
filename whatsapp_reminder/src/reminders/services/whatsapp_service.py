import requests
from django.conf import settings
from typing import Optional, Dict, Any
from decouple import config as env


class GreenAPIService:
    """
    Инициализирую сервис для отправки сообщений через GreenAPI
    """
    def __init__(self):
        self.base_url = env("GREEN_API_BASE_URL")
        self.id_instance = env("GREEN_API_ID_INSTANCE")
        self.api_token_instance = env("GREEN_API_TOKEN_INSTANCE")
        self.phone_number = env("GREEN_API_PHONE_NUMBER")
        self.headers = {
            'Authorization': f'Bearer {self.api_token_instance}',
            'Content-Type': 'application/json'
        }


    """
    Метод для отправки сообщения
    """
    def send_message(self, phone_number: str, message: str) -> Optional[Dict[str, Any]]:
        url = f"{self.base_url}/waInstance{self.id_instance}/SendMessage/{self.api_token_instance}"

        payload = {
            "chatId": f"{phone_number}@c.us",
            "message": message
        }
        response = requests.post(url, json=payload, headers=self.headers)
        return response.json()


    """
    Метод для получения статуса сообщения
    """
    def get_message_status(self, message_id):
        url = f"{self.base_url}/waInstance{self.id_instance}/GetMessageStatus/{self.api_token_instance}"
        params = {
            "id": message_id
        }
        response = requests.get(url, params=params, headers=self.headers)
        return response.json()
