from rest_framework import serializers
from .models import UserDetails, Company, Job, Applications

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ['id', 'jobTitle', 'jobUrl', 'companyName', 'location', 'jobDescription']


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['company_id', 'company_name', 'company_description']

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['job_id', 'job_title', 'job_url', 'company_id', 'job_location', 'job_description']
    

class ApplicationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applications
        fields = ['application_id', 'user_id', 'job_id']

def get_serializer_class(model_name):
     if model_name == 'UserDetails':
        return UserDetailsSerializer
     elif model_name == 'Company':
        return CompanySerializer
     elif model_name == 'Job':
        return JobSerializer
     elif model_name == 'Applications':
        return ApplicationsSerializer    
     else:
        raise ValueError(f"No serializer found for model '{model_name}'")
