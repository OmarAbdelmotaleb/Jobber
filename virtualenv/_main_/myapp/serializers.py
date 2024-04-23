from rest_framework import serializers
from .models import Company, Job, Applications, Users


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['company_id', 'name', 'industry', 'location', 'website', 'linkedin']


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['user_id', 'name', 'email', 'password']


class JobSerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())
    class Meta:
        model = Job
        fields = ['job_id', 'job_title', 'job_url', 'company', 'job_location', 'job_description']
    

class ApplicationsSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all())
    job = serializers.PrimaryKeyRelatedField(queryset=Job.objects.all())
    class Meta:
        model = Applications
        fields = ['application_id', 'user', 'job']

def get_serializer_class(model_name):
     if model_name == 'Company':
        return CompanySerializer
     elif model_name == 'Job':
        return JobSerializer
     elif model_name == 'Users':
        return UsersSerializer
     elif model_name == 'Applications':
        return ApplicationsSerializer    
     else:
        raise ValueError(f"No serializer found for model '{model_name}'")
