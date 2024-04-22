from rest_framework import serializers
from .models import Users, Company, Applications, Contacts
# NOTE: Removed Job

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['user_id', 'name', 'email', 'password']


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['company_id', 'company_name', 'company_description']

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'

        extra_kwargs = {
            'name': {'required': False},
            'loc': {'required': False},
            'desc': {'required': False},
            'status': {'required': False},
            'company': {'required': False},
            'email': {'required': False},
            'phone': {'required': False},
            'relationship': {'required': False},
            'link': {'required': False},
            'follow_up_date': {'required': False},
        }

class ApplicationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applications
        fields = '__all__'

        extra_kwargs = {
            'max_salary': {'required': False},
            'min_salary': {'required': False},
            'date_applied': {'required': False},
            'follow_up_date': {'required': False},
            'notes': {'required': False},
            'user': {'required': False}
            # Add similar entries for other optional fields (user might be a related field)
        }

def get_serializer_class(model_name):
     if model_name == 'Users':
        return UsersSerializer
     elif model_name == 'Company':
        return CompanySerializer
     elif model_name == 'Applications':
        return ApplicationsSerializer    
     else:
        raise ValueError(f"No serializer found for model '{model_name}'")
     
