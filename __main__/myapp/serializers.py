from rest_framework import serializers
from .models import UserDetails

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ['id', 'name', 'degree', 'jobProfile', 'schoolName']

def get_serializer_class():
    from .serializers import UserDetailsSerializer
    return UserDetailsSerializer
