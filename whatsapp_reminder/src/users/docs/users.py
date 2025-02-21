from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from users.api.serializers import (
    UserProfileResponseSerializer,
    ErrorResponseSerializer,
    SuccessResponseSerializer,
    UserUpdateSerializer,
)

user_profile_schema = extend_schema(
    summary="Получение профиля пользователя",
    description="""
    Возвращает информацию о пользователе по номеру телефона.
    Включает:
    - Информацию о пользователе
    - Количество напоминаний
    """,
    parameters=[
        OpenApiParameter(
            name="phone_number",
            location=OpenApiParameter.PATH,
            description="Номер телефона пользователя (формат: +7XXXXXXXXXX)",
            required=True,
            type=str
        ),
    ],
    responses={
        200: UserProfileResponseSerializer,
        404: ErrorResponseSerializer
    },
    examples=[
        OpenApiExample(
            "Успешный ответ",
            value={
                "phone_number": "+79991234567",
                "created_at": "2024-02-21T10:00:00Z",
                "is_active": True,
                "reminders_count": 5
            },
            status_codes=["200"]
        ),
        OpenApiExample(
            "Пользователь не найден",
            value={
                "error": "User not found"
            },
            status_codes=["404"]
        )
    ]
)



user_update_schema = extend_schema(
    summary="Обновление профиля пользователя",
    description="""
    Обновляет данные пользователя по номеру телефона.
    
    Доступные поля для обновления:
    - is_active
    - last_interaction
    """,
    parameters=[
        OpenApiParameter(
            name="phone_number",
            location=OpenApiParameter.PATH,
            description="Номер телефона пользователя (формат: +7XXXXXXXXXX)",
            required=True,
            type=str
        ),
    ],
    request=UserUpdateSerializer,
    responses={
        200: SuccessResponseSerializer,
        400: ErrorResponseSerializer,
        404: ErrorResponseSerializer
    },
    examples=[
        OpenApiExample(
            "Успешное обновление",
            value={
                "message": "User updated successfully"
            },
            status_codes=["200"]
        ),
        OpenApiExample(
            "Ошибка валидации",
            value={
                "error": "Invalid data provided"
            },
            status_codes=["400"]
        ),
        OpenApiExample(
            "Пользователь не найден",
            value={
                "error": "User not found"
            },
            status_codes=["404"]
        )
    ]
)
