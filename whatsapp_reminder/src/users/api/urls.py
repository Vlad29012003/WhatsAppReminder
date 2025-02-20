from django.urls import path
from .views import UserProfileView , UserUpdateView

urlpatterns = [
    path('user/profile/<str:phone_number>/', UserProfileView.as_view(), name='user-profile'),
    path('user/update/<str:phone_number>/', UserUpdateView.as_view(), name='user-update'),
]
