from django.urls import path
from . import views
from .views import UserDetailsAPIView, CompanyListCreateAPIView, JobListCreateAPIView

urlpatterns = [
    path('api/userdetails/create/', UserDetailsAPIView.as_view(), name='userdetails-create'),
    path('api/userdetails/<int:pk>/', UserDetailsAPIView.as_view(), name='userdetails-update'),
    path('api/userdetails/', UserDetailsAPIView.as_view(), name='userdetails-list'),
    path('companies/', CompanyListCreateAPIView.as_view(), name='company-list-create'),
    path('companies/<int:pk>/', CompanyListCreateAPIView.as_view(), name='company-detail'),
    path('jobs/', JobListCreateAPIView.as_view(), name='job-list-create'),
    path('jobs/<int:pk>/', JobListCreateAPIView.as_view(), name='job-detail'),
]
