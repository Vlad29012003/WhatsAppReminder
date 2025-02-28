import dateutil
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from reminders.api.serializers import ReminderSerializer
from users.models import User
from reminders.models import Reminder
from reminders.services.whatsapp_service import GreenAPIService
from drf_spectacular.utils import extend_schema, extend_schema_view , OpenApiResponse, OpenApiExample
from reminders.docs.schemas import reminder_create_schema, reminder_list_schema, reminder_delete_schema


class WebhookView(APIView):
    """
    Обработка входящих сообщений от GreenAPI через вебхук
    """
    def post(self, request):
        data = request.data
        print("Webhook data:", data)

        # Получаем receiptId для удаления уведомления
        receipt_id = data.get("receiptId")
        green_api = GreenAPIService()

        if data.get("typeWebhook") == "incomingMessageReceived":
            sender = data["senderData"]["sender"]
            phone_number = sender.split("@")[0]
            message = data["messageData"]["textMessageData"]["textMessage"]

            try:
                parts = message.split(" в ")
                if len(parts) < 2:
                    raise ValueError("Формат: Напомни в YYYY-MM-DD HH:MM текст")
                text = parts[0].replace("Напомни", "").strip()
                scheduled_time = dateutil.parser.parse(parts[1].strip())

                # Создаем пользователя и напоминание
                user, _ = User.objects.get_or_create(phone_number=phone_number)
                reminder = Reminder.objects.create(
                    user=user,
                    text=text,
                    scheduled_time=scheduled_time,
                    is_sent=False
                )

                # Отправляем подтверждение
                green_api.send_message(phone_number, f"Напоминание создано: {text} на {scheduled_time}")

                # Удаляем уведомление после успешной обработки
                if receipt_id:
                    green_api.delete_notification(receipt_id)
                return Response({"status": "ok"}, status=200)

            except Exception as e:
                # Отправляем сообщение об ошибке
                green_api.send_message(phone_number, f"Ошибка: {str(e)}. Пример: Напомни в 2025-02-21 04:30 тест")
                
                # Удаляем уведомление даже в случае ошибки, чтобы не застревало
                if receipt_id:
                    green_api.delete_notification(receipt_id)
                return Response({"status": "error"}, status=400)

        # Удаляем уведомление, если оно не "incomingMessageReceived"
        if receipt_id:
            green_api.delete_notification(receipt_id)
        return Response({"status": "ignored"}, status=200)



class CreateReminderView(APIView):
    """
    Метод для создания напоминания
    """

    @extend_schema(
        request=ReminderSerializer,
        responses={201: reminder_create_schema},
        tags=['Reminders']
    )

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
    



class ListRemindersView(APIView):
    """
    Метод для получения списка напоминаний
    """

    @extend_schema(
        responses={200: reminder_list_schema},
        tags=['Reminders']
    )

    def get(self, request, phone_number):
        user = User.objects.filter(phone_number=phone_number).first()
        if not user:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        reminders = Reminder.objects.filter(user=user)
        serializer = ReminderSerializer(reminders, many=True)
        return Response(serializer.data)



class DeleteReminderView(APIView):
    """
    Метод для удаления напоминания
    """
    @extend_schema(
        responses={204: reminder_delete_schema},
        tags=['Reminders']
    )

    def delete(self, request, reminder_id):
        reminder = Reminder.objects.filter(id=reminder_id).first()
        if not reminder:
            return Response({"message": "Reminder not found"}, status=status.HTTP_404_NOT_FOUND)
        
        reminder.delete()
        return Response({"message": "Reminder deleted successfully"}, status=status.HTTP_204_NO_CONTENT)






