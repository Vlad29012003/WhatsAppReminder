from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import User
from reminders.models import Reminder
from reminders.services.whatsapp_service import GreenAPIService


class CreateReminderView(APIView):
    """
    Метод для создания напоминания
    """
    def post(self, request):
        phone_number = request.data.get('phone_number')
        text = request.data.get('text')
        scheduled_time = request.data.get('scheduled_time')

        user, created = User.objects.get_or_create(phone_number=phone_number)
        reminder = Reminder.objects.create(
            user=user,
            text=text,
            scheduled_time=scheduled_time
        )

        green_api = GreenAPIService()
        confirmation_message = f"Напоминание создано: {text} на {scheduled_time}"
        green_api.send_message(phone_number, confirmation_message)

        return Response({"message": "Reminder created successfully"}, status=status.HTTP_201_CREATED)













