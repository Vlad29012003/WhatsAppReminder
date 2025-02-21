from rest_framework import serializers
from users.models import User

class UserUpdateSerializer(serializers.ModelSerializer):
    """
    Сериализатор для обновления данных пользователя
    """
    phone_number = serializers.CharField(
        help_text="Номер телефона пользователя",
        read_only=True
    )
    is_active = serializers.BooleanField(
        help_text="Статус активности пользователя"
    )
    last_itteraction = serializers.DateTimeField(
        help_text="Время последнего взаимодействия с пользователем",
        required=False
    )

    class Meta:
        model = User
        fields = ['phone_number', 'is_active', 'last_itteraction']




class UserProfileResponseSerializer(serializers.Serializer):
    """
    Сериализатор для ответа с данными профиля пользователя
    """
    phone_number = serializers.CharField(
        help_text="Номер телефона пользователя"
    )
    created_at = serializers.DateTimeField(
        help_text="Дата и время создания пользователя"
    )
    is_active = serializers.BooleanField(
        help_text="Статус активности пользователя"
    )
    reminders_count = serializers.IntegerField(
        help_text="Общее количество напоминаний пользователя"
    )


class ErrorResponseSerializer(serializers.Serializer):
    """
    Сериализатор для ответов с ошибками
    """
    error = serializers.CharField(
        help_text="ошибка"
    )


class SuccessResponseSerializer(serializers.Serializer):
    """
    Сериализатор для успешных ответов
    """
    message = serializers.CharField(
        help_text="Текст сообщения об успешном выполнении операции"
    )




class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone_number', 'is_active', 'last_itteraction']
