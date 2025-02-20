from django.urls import path
from .views import CreateReminderView , DeleteReminderView , ListRemindersView

urlpatterns = [
    path('create-reminder/', CreateReminderView.as_view(), name='create-reminder'),
    path('delete-reminder/<int:reminder_id>/', DeleteReminderView.as_view(), name='delete-reminder'),
    path('list-reminder/<str:phone_number>/', ListRemindersView.as_view(), name='list-reminder'),

]
