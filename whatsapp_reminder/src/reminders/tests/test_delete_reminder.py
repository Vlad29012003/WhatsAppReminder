import pytest
from rest_framework import status
from rest_framework.test import APIClient

client = APIClient()

@pytest.mark.django_db
def test_delete_reminder(create_user, create_reminder):
    """
    Тест эндпоинта для удаления напоминания.
    """
    url = f"/api/reminders/delete-reminder/{create_reminder.id}/"
    response = client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_delete_reminder_not_found():
    """
    Тест, если напоминание не найдено при удалении.
    """
    url = "/api/reminders/delete-reminder/999/"
    response = client.delete(url)

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.data == {"message": "Reminder not found"}