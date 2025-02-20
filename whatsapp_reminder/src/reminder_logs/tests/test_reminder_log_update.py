import pytest
from rest_framework import status
from rest_framework.test import APIClient
from reminder_logs.models import ReminderLog
from reminders.models import Reminder


class TestReminderLogUpdateView:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.client = APIClient()

    @pytest.mark.django_db
    def test_update_reminder_log(self, create_reminder_log):
        """
        Тест обновления информации о логе напоминания.
        """
        log = create_reminder_log
        url = f"/api/reminder_logs/logs/update/{log.id}/"
        updated_data = {"status": "completed", "error_message": "No errors"}

        response = self.client.patch(url, updated_data)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["message"] == "log updated successfully"
        
        log.refresh_from_db()
        assert log.status == updated_data["status"]
        assert log.error_message == updated_data["error_message"]


    @pytest.mark.django_db
    def test_update_reminder_log_not_found(self):
        """
        Тест получения ошибки, если лог не найден для обновления.
        """
        url = "/api/reminder_logs/logs/update/9999/"
        updated_data = {"status": "completed", "error_message": "No errors"}

        response = self.client.patch(url, updated_data)

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.data == {"error": "log not found"}