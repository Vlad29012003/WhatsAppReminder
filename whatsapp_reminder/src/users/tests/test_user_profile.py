import pytest
from rest_framework import status
from rest_framework.test import APIClient
from users.models import User
from reminders.models import Reminder

class TestUserProfileView:

    """
    Тест на получение профиля пользователя
    """
    @pytest.mark.django_db
    def test_get_user_profile(self, create_user , create_reminder):
        client = APIClient()
        url = f'/api/users/user/profile/{create_user.phone_number}/'
        response = client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data['phone_number'] == create_user.phone_number
        assert response.data['is_active'] == create_user.is_active
        assert response.data['reminders_count'] == 1


    """
    Тест на получение профиля пользователя, если пользователь не найден
    """
    @pytest.mark.django_db
    def test_get_user_profile_not_found(self):
        client = APIClient()
        url = f'/api/users/user/profile/123/'
        response = client.get(url)

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.data['error'] == 'User not found'    


    


