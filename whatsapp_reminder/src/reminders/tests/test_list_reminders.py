import pytest
from rest_framework import status
from rest_framework.test import APIClient
from users.models import User
from reminders.models import Reminder
from unittest.mock import patch, Mock

client = APIClient()


@pytest.mark.django_db
def test_list_reminders(create_user, create_reminder):
    """
    Тест эндпоинта для получения списка напоминаний.
    """
    url = f"/api/reminders/list-reminder/{create_user.phone_number}/"


    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]["text"] == "Test reminder"


@pytest.mark.django_db
def test_list_reminders_user_not_found():
    """
    Тест, если пользователь не найден при получении списка напоминаний.
    """
    url = "/api/reminders/list-reminder/+11111111111/"


    response = client.get(url)

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.data == {"error": "User not found"}
