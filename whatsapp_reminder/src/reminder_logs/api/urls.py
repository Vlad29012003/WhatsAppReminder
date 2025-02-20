from django.urls import path
from .views import ReminderLogListView , ReminderLogDetailView , ReminderLogUpdateView

urlpatterns = [
    path('logs/', ReminderLogListView.as_view(), name='reminder-log-list'),
    path('logs/<int:log_id>/', ReminderLogDetailView.as_view(), name='reminder-log-detail'),
    path('logs/update/<int:log_id>/', ReminderLogUpdateView.as_view(), name='reminder-log-update'),

    
]
