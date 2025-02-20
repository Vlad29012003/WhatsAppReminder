import pytest
from rest_framework.test import APIClient
from reminder_logs.models import ReminderLog
from reminders.models import Reminder
from users.models import User


@pytest.fixture
def client():
    """
    Фикстура для клиента API.
    """
    return APIClient()



@pytest.fixture
def create_user(db):
    """
    Создание тестового пользователя.
    """
    return User.objects.create(phone_number="+996700828128")



@pytest.fixture
def create_reminder(create_user):
    """Создание тестового напоминания."""
    return Reminder.objects.create(
        user=create_user,
        text="Test reminder",
        scheduled_time="2025-02-25T10:00:00Z"
    )


@pytest.fixture
def create_reminder_log(create_reminder):
    """
    Создание тестового лога напоминания.
    """
    return ReminderLog.objects.create(
        reminder=create_reminder,
        status="pending",
    )