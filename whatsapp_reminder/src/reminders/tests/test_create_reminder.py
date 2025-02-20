import pytest
from rest_framework import status
from rest_framework.test import APIClient
from users.models import User
from reminders.models import Reminder
from unittest.mock import patch, Mock


client = APIClient()


class TestReminderViews:

    @pytest.mark.django_db
    @patch("reminders.services.whatsapp_service.GreenAPIService.send_message")
    def test_create_reminder(self, mock_send_message, create_user):
        """
        Тест на создания напоминания.
        """

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"message": "Message sent successfully"}
        mock_send_message.return_value = {"message": "Message sent successfully"}

        url = "/api/reminders/create-reminder/"


        data = {
            "phone_number": create_user.phone_number,
            "text": "Hello from test!",
            "scheduled_time": "2024-10-30T15:00:00Z",
        }

        response = client.post(url, data, format="json")

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["message"] == "Reminder created successfully"
        assert Reminder.objects.filter(text="Hello from test!").exists()
        mock_send_message.assert_called_once_with(
            create_user.phone_number, 
            "Напоминание создано: Hello from test! на 2024-10-30T15:00:00Z"
        )






