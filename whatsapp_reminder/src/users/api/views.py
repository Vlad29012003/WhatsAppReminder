from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import User
from reminders.models import Reminder
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter, OpenApiResponse, OpenApiExample
from users.api.serializers import UserProfileResponseSerializer, ErrorResponseSerializer, SuccessResponseSerializer , UserUpdateSerializer
from users.docs.users import user_profile_schema , user_update_schema


@extend_schema_view(
    get=user_profile_schema,
    tags=['Users']
)
class UserProfileView(APIView):
    """
    Эндпоинт для получения информации о пользователе
    """

    def get(self, request, phone_number):
        user = User.objects.filter(phone_number=phone_number).first()
        if not user:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
        total_reminders = Reminder.objects.filter(user=user).count()

        user_data = {
            "phone_number": user.phone_number,
            "created_at": user.created_at,
            "is_active": user.is_active,
            "reminders_count": total_reminders,
        }
        return Response(user_data)
    


@extend_schema_view(
    get=user_update_schema,
    tags=['Users']
)

class UserUpdateView(APIView):
    """
    Эндпоинт для обновления информации о пользователе
    """

    def patch(self, request, phone_number):
        user = User.objects.filter(phone_number=phone_number).first()
        if not user:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        

        serializer = UserUpdateSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        