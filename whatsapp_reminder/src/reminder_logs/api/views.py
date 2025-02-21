from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from reminder_logs.models import ReminderLog
from .serializers import ReminderLogSerializer
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiResponse, OpenApiExample
from reminder_logs.docs.schemas import reminder_log_list_schema, reminder_log_detail_schema, reminder_log_update_schema



class ReminderLogListView(APIView):
    """
    Метод для получения списка логов напоминаний
    """
    @extend_schema(
        responses={200: reminder_log_list_schema},
        tags=['Reminder Logs']
    )
    def get(self, request):
        reminder_logs = ReminderLog.objects.all()
        serializer = ReminderLogSerializer(reminder_logs, many=True)
        return Response(serializer.data)
    

class ReminderLogDetailView(APIView):
    """
    Метод для получения информации о логе напоминания
    """
    @extend_schema(
        responses={200: reminder_log_detail_schema},
        tags=['Reminder Logs']
    )
    def get(self, request, log_id):
        log = ReminderLog.objects.filter(id=log_id).first()
        if not log:
            return Response({"error": "log not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ReminderLogSerializer(log)
        return Response(serializer.data)
    
    
class ReminderLogUpdateView(APIView):
    """
    Метод для обновления информации о логе напоминания
    """
    
    def patch(self, request, log_id):
        log = ReminderLog.objects.filter(id=log_id).first()
        if not log:
            return Response({"error": "log not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ReminderLogSerializer(log, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "log updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
