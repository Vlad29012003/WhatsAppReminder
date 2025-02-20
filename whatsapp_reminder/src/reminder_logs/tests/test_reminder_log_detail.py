import pytest
from rest_framework import status
from rest_framework.test import APIClient
from reminder_logs.models import ReminderLog

class TestReminderLogDetailView:


    @pytest.fixture(autouse=True)
    def setup(self):
        self.client = APIClient()

    
    @pytest.mark.django_db
    def test_get_reminder_log(self, create_reminder_log):
        """
        Тест получения информации о логе напоминания по ID.
        """
        log = create_reminder_log 
        url = f"/api/reminder_logs/logs/{log.id}/"
        response = self.client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["id"] == log.id
        assert response.data["status"] == log.status
        assert response.data["error_message"] == log.error_message


    @pytest.mark.django_db
    def test_get_reminder_log_not_found(self):
        """
        Тест получения ошибки, если лог не найден.
        """
        url = "/api/reminder_logs/logs/9999/"
        response = self.client.get(url)

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.json() == {"error": "log not found"}

