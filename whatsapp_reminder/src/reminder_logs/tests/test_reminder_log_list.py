import pytest
from rest_framework import status
from rest_framework.test import APIClient

class TestReminderLogListView:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.client = APIClient()

    @pytest.mark.django_db
    def test_get_reminder_logs(self, create_reminder_log):
        """
        Тест получения списка логов напоминаний.
        """
        url = "/api/reminder_logs/logs/"
        response = self.client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]["status"] == "pending"
        assert response.data[0]["error_message"] is None 

    @pytest.mark.django_db
    def test_get_reminder_logs_empty(self):
        """
        Тест получения пустого списка логов, если логов нет.
        """
        url = "/api/reminder_logs/logs/"
        response = self.client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data == []