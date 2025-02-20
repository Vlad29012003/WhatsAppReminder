from django.db import models
from reminders.models import Reminder


class ReminderLog(models.Model):
    reminder = models.ForeignKey(Reminder, on_delete=models.CASCADE, related_name='logs')
    sent_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10)
    error_message = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-sent_at']

    def __str__(self):
        return f'{self.reminder_id} - {self.sent_at}'


