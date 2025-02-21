from drf_spectacular.utils import OpenApiResponse, OpenApiExample
from reminders.api.serializers import ReminderSerializer


reminder_create_schema = OpenApiResponse(
    description="Напоминание создано успешно",
    response=ReminderSerializer,
    examples=[
        OpenApiExample('Пример создания напоминания', value={
            "message": "Напоминание создано успешно"
        })
    ]
)




reminder_list_schema = OpenApiResponse(
    description="Список напоминаний пользователя", 
    response=ReminderSerializer,
    examples=[
        OpenApiExample('List reminders example', value=[
            {
                "id": 1,
                "user": 123456789,
                "text": "Meeting at 10:00 AM",
                "scheduled_time": "2025-02-21T10:00:00Z",
                "status": "pending",
                "repeat_type": "none",
                "last_sent": None
            },
            {
                "id": 2,
                "user": 123456789,
                "text": "Lunch at 12:00 PM",
                "scheduled_time": "2025-02-21T12:00:00Z",
                "status": "sent",
                "repeat_type": "daily",
                "last_sent": "2025-02-21T12:00:00Z"
            }
        ])
    ]
)


reminder_delete_schema = OpenApiResponse(
    description="Напоминание удалено успешно",
    response=None,
    examples=[
        OpenApiExample('Пример удаления напоминания', value={
            "message": "Напоминание удалено успешно"
        })
    ]
)