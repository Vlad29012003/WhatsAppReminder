import pytest
from users.models import User
from reminders.models import Reminder

@pytest.fixture
def create_user():
    """
    Создание тестового пользователя.
    """
    return User.objects.create(phone_number="+996707828028", is_active=True)



@pytest.fixture
def create_reminder(create_user):
    """
    Создание тестового напоминания.
    """
    return Reminder.objects.create(
        user=create_user, 
        text="Test reminder", 
        scheduled_time="2024-10-30T15:00:00Z"
    )
