import pytest
from users.models import User
from reminders.models import Reminder


@pytest.fixture
def create_user():
    user = User.objects.create(phone_number='+996707828028', is_active=True)
    return user

@pytest.fixture
def create_reminder(create_user):
    reminder = Reminder.objects.create(user=create_user, text='Test reminder', scheduled_time='2025-02-19 12:00')
    return reminder
