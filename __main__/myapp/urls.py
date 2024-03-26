from django.urls import path
from . import views
from .views import UserDetailsAPIView

urlpatterns = [
    path('api/userdetails/create/', UserDetailsAPIView.as_view(), name='userdetails-create'),
    path('api/userdetails/<int:pk>/', UserDetailsAPIView.as_view(), name='userdetails-update'),
    path('api/userdetails/', UserDetailsAPIView.as_view(), name='userdetails-list')
]
