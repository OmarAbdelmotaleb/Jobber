from django.urls import path
from . import views
from .views import UsersAPIView, CompanyListCreateAPIView, ApplicationListAPIView, ApplicationCreateAPIView, ContactsCreateAPIView

urlpatterns = [
    path('companies/', CompanyListCreateAPIView.as_view(), name='company-list-create'),
    path('companies/<int:pk>/', CompanyListCreateAPIView.as_view(), name='company-detail'),
    path('applications/', ApplicationListAPIView.as_view(), name='applications-list-create'),
    path('applications/<int:pk>/', ApplicationListAPIView.as_view(), name='application-detail'),
    path('users/', UsersAPIView.as_view(), name='users-list-create'),
    path('users/<int:pk>/', UsersAPIView.as_view(), name='users-detail'),
    path('job-applications/', ApplicationCreateAPIView.as_view(), name='job-application-create'),
    path('contacts/', ContactsCreateAPIView.as_view(), name='contacts-list-create'),
    path('contacts/<int:pk>/', ContactsCreateAPIView.as_view(), name='contacts-detail'),
]
