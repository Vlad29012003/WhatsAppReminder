from django.urls import path
from .views import CreateReminderView

urlpatterns = [
    path('create-reminder/', CreateReminderView.as_view(), name='create-reminder'),

]
