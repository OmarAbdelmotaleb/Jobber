from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from .models import Users, Company, Applications, Contacts
from .serializers import UsersSerializer, ApplicationsSerializer, CompanySerializer, ContactsSerializer  # Importing serializer
from django.http import Http404
# NOTE: Removed JobSerializer from Serializers and Job from Models

class UsersAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            try:
                user = Users.objects.get(pk=pk)
                serializer = UsersSerializer(user)
                return Response(serializer.data)
            except Users.DoesNotExist:
                raise Http404
        else:
            users = Users.objects.all()
            serializer = UsersSerializer(users, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            user = Users.objects.get(pk=pk)
        except Users.DoesNotExist:
            raise Http404

        serializer = UsersSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            user = Users.objects.get(pk=pk)
        except Users.DoesNotExist:
            raise Http404

        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

     # Add methods for Company CRUD operations
class CompanyListCreateAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            try:
                company = Company.objects.get(pk=pk)
                serializer = CompanySerializer(company)
                return Response(serializer.data)
            except Company.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            companies = Company.objects.all()
            serializer = CompanySerializer(companies, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        company = Company.objects.get(pk=pk)
        serializer = CompanySerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            company = Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

     # Add methods for Job CRUD operations
    

class ContactsCreateAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            try:
                contact = Contacts.objects.get(pk=pk)
                serializer = ContactsSerializer(contact)
                return Response(serializer.data)
            except Contacts.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            contact = Contacts.objects.all()
            serializer = ContactsSerializer(contact, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = ContactsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        contact = Contacts.objects.get(pk=pk)
        serializer = ContactsSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            contact = Contacts.objects.get(pk=pk)
        except Contacts.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

     # Add methods for Job CRUD operations

class ApplicationListAPIView(APIView):
    def get(self, request):
        applications = Applications.objects.all()
        serializer = ApplicationsSerializer(applications, many=True)

        response_data = serializer.data

        for application in response_data:
            if isinstance(application['date_applied'], str):
                application['dateApplied'] = datetime.strptime(application['date_applied'], '%Y-%m-%d').strftime('%m/%d/%Y')
            else:
                application['dateApplied'] = application['date_applied'].strftime('%m/%d/%Y')

            if application['follow_up_date']:
                if isinstance(application['follow_up_date'], str):
                    application['followUpDate'] = datetime.strptime(application['follow_up_date'], '%Y-%m-%d').strftime('%m/%d/%Y')
                else:
                    application['followUpDate'] = application['follow_up_date'].strftime('%m/%d/%Y')
            else:
                application['followUpDate'] = None

        return Response(response_data)
    
    def post(self, request):
        serializer = ApplicationsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):

        try:
            applications = Applications.objects.get(pk=pk)
        except Applications.DoesNotExist:
            raise Http404

        serializer = ApplicationsSerializer(applications, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            applications = Applications.objects.get(pk=pk)
        except Applications.DoesNotExist:
            raise Http404

        applications.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ApplicationCreateAPIView(APIView):
    def post(self, request):
        serializer = ApplicationsSerializer(data=request.data) 
        if serializer.is_valid():
            default_user, _ = Users.objects.get_or_create(name='John Doe')
            serializer.validated_data['user'] = default_user

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)