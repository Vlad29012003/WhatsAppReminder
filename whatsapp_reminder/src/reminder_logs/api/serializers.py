from rest_framework import serializers
from reminder_logs.models import ReminderLog


class ReminderLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReminderLog
        fields = ['reminder', 'sent_at', 'status', 'error_message']
