from celery import shared_task
from django.utils import timezone
from .models import Reminder
from reminders.services.whatsapp_service import GreenAPIService

@shared_task
def send_scheduled_reminders():
    """
    Задача для отправки напоминаний, у которых наступило время.
    """
    current_time = timezone.now()
    reminders = Reminder.objects.filter(
        scheduled_time__lte=current_time,
        is_sent=False
    )
    green_api = GreenAPIService()

    for reminder in reminders:
        green_api.send_message(reminder.user.phone_number, reminder.text)
        reminder.is_sent = True
        reminder.save()

    return f"Processed {len(reminders)} reminders"

@shared_task
def schedule_reminder(reminder_id):
    """
    Задача для отправки конкретного напоминания в указанное время.
    """
    reminder = Reminder.objects.get(id=reminder_id)
    green_api = GreenAPIService()
    green_api.send_message(reminder.user.phone_number, f"Напоминание: {reminder.text}")
    reminder.delete()