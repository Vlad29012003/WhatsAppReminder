import pytest
from rest_framework import status
from rest_framework.test import APIClient
from users.models import User
from reminders.models import Reminder

class TestUserUpdateView:

    @pytest.mark.django_db
    def test_update_user(self, create_user):
        """
        Тест на обновление пользователя
        """
        client = APIClient()
        url = f'/api/users/user/update/{create_user.phone_number}/'
        data = {
            'is_active': False
        }
        response = client.patch(url, data, format='json')


        assert response.status_code == status.HTTP_200_OK
        assert response.data["message"] == "User updated successfully"
        create_user.refresh_from_db()
        assert create_user.is_active == False


    @pytest.mark.django_db
    def test_update_user_not_found(self):
        """
        Тест на обновление пользователя, если пользователь не найден
        """
        client = APIClient()
        url = '/api/users/user/update/123/'
        data = {
            'is_active': False
        }
        response = client.patch(url, data, format='json')

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.data == {"error": "User not found"}


    @pytest.mark.django_db
    def test_update_user_invalid_data(self, create_user):
        """
        Тест на обновление пользователя с неправильными данными
        """
        client = APIClient()
        url = f'/api/users/user/update/{create_user.phone_number}/'
        data = {
            'is_active': 'invalid'
        }
        response = client.patch(url, data, format='json')

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data == {'is_active': ['Must be a valid boolean.']}



