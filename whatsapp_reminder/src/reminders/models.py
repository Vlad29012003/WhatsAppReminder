from django.db import models
from users.models import User


class Reminder(models.Model):
    REMINDER_STATUS = (
        ('pending', 'Pending'),
        ('sent', 'Sent'),
        ('failed', 'Failed'),
        ('cancelled', 'Cancelled')
    )

    REPEAT_CHOICES = (
        ('none', 'No repeat'),
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reminders')
    text = models.TextField()
    scheduled_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=REMINDER_STATUS, default='pending')
    repeat_type = models.CharField(max_length=10, choices=REPEAT_CHOICES, default='none')
    last_sent = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-scheduled_time']
        indexes = [
            models.Index(fields=['scheduled_time', 'status']),
            models.Index(fields=['user' , 'status'])]
        
    def __str__(self):
        return f'{self.user.phone_number} - {self.scheduled_time}'
    
    







