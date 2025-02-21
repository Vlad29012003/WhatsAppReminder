from drf_spectacular.utils import OpenApiResponse, OpenApiExample
from reminder_logs.api.serializers import ReminderLogSerializer



reminder_log_list_schema = OpenApiResponse(
    description="Список логов напоминаний",
    response=ReminderLogSerializer,
    examples=[
        OpenApiExample('List reminder logs example', value=[
            {
                "id": 1,
                "reminder": 1,
                "status": "sent",
                "timestamp": "2025-02-21T10:00:00Z",
                "message": "Message sent to user"
            },
            {
                "id": 2,
                "reminder": 2,
                "status": "failed",
                "timestamp": "2025-02-21T12:00:00Z",
                "message": "Failed to send message"
            }
        ])
    ]
)


reminder_log_detail_schema = OpenApiResponse(
    description="Информация о логе напоминания",
    response=ReminderLogSerializer,
    examples=[
        OpenApiExample('Reminder log detail example', value={
            "id": 1,
            "reminder": 1,
            "status": "sent",
            "timestamp": "2025-02-21T10:00:00Z",
            "message": "Message sent to user"
        })
    ]
)

reminder_log_update_schema = OpenApiResponse(
    description="Информация о обновлении лога напоминания",
    response=ReminderLogSerializer,
    examples=[
        OpenApiExample('Updated reminder log example', value={
            "id": 1,
            "reminder": 1,
            "status": "sent",
            "timestamp": "2025-02-21T10:00:00Z",
            "message": "Message sent to user"
        })
    ]
)