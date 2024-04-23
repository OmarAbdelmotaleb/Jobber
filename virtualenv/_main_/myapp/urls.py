from django.urls import path
from . import views
from .views import CompanyListCreateAPIView, JobListCreateAPIView, ApplicationsAPIView, UsersAPIView, ApplicationCopareAPIView

urlpatterns = [
    path('companies/', CompanyListCreateAPIView.as_view(), name='company-list-create'),
    path('companies/<int:pk>/', CompanyListCreateAPIView.as_view(), name='company-detail'),
    path('jobs/', JobListCreateAPIView.as_view(), name='job-list-create'),
    path('jobs/<int:pk>/', JobListCreateAPIView.as_view(), name='job-detail'),
    path('applications/', ApplicationsAPIView.as_view(), name='applications-list-create'),
    path('applications/<int:pk>/', ApplicationsAPIView.as_view(), name='application-detail'),
    path('users/', views.UsersAPIView.as_view(), name='users-list-create'),
    path('users/<int:pk>/', views.UsersAPIView.as_view(), name='user-detail'),
    path('application/compare/', ApplicationCopareAPIView.as_view(), name='application-compare')
]
