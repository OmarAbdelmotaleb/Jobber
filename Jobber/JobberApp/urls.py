from django.urls import path
from . import views
from .views import UsersAPIView, CompanyListCreateAPIView, ApplicationListAPIView

urlpatterns = [
    path('companies/', CompanyListCreateAPIView.as_view(), name='company-list-create'),
    path('companies/<int:pk>/', CompanyListCreateAPIView.as_view(), name='company-detail'),
    path('applications/', ApplicationListAPIView.as_view(), name='applications-list'),
    path('users/', views.UsersAPIView.as_view(), name='users-list-create'),
    path('users/<int:pk>/', views.UsersAPIView.as_view(), name='user-detail'),
]
