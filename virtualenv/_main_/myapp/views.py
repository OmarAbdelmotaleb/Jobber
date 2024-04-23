from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Company, Job, Applications, Users, Resume
from .serializers import JobSerializer, CompanySerializer, ApplicationsSerializer, UsersSerializer  # Importing serializer

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
class JobListCreateAPIView(APIView):
    def get(self, request, pk=None):
         if pk is not None:
            try:
                job = Job.objects.get(pk=pk)
                serializer = JobSerializer(job)
                company_id = serializer.data['company'] 
                company = Company.objects.get(pk=company_id) 
                company_data = {'company_name': company.company_name, 'company_description': company.company_description}
                serializer.data['company'] = company_data 
                return Response(serializer.data)
            except Job.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
         else:
            jobs = Job.objects.all()
            serializer = JobSerializer(jobs, many=True)
            for job_data in serializer.data:
                company_id = job_data['company'] 
                company = Company.objects.get(pk=company_id) 
                company_data = {'company_name': company.company_name, 'company_description': company.company_description}
                job_data['company'] = company_data  

            return Response(serializer.data)
    def post(self, request):
        serializer = JobSerializer(data=request.data)
        print(serializer, 'check data>>>>>>..')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        job = Job.objects.get(pk=pk)
        serializer = JobSerializer(job, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            job = Job.objects.get(pk=pk)
        except Job.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ApplicationsAPIView(APIView):
    def get(self, request, pk=None):
       if pk is not None:
            try:
                application = Applications.objects.get(pk=pk)
                serializer = ApplicationsSerializer(application)
                user_id = serializer.data['user'] 
                user = Users.objects.get(pk=user_id) 
                user_data = {'user_id': user.user_id, 'name': user.name, 'email': user.email}
                serializer.data['user'] = user_data 
                job_id = serializer.data['job'] 
                job = Job.objects.get(pk=job_id) 
                job_data = {'job_id': job.job_id, 'job_title': job.job_title, 'job_url': job.job_url, 'company': {'company_id': job.company.company_id, 'company_name': job.company.company_name, 'company_description': job.company.company_description}, 'job_location': job.job_location, 'job_description': job.job_description}
                serializer.data['job'] = job_data 
                return Response(serializer.data)
            except Applications.DoesNotExist:
                raise Http404
       else:
            applications = Applications.objects.all()
            serializer = ApplicationsSerializer(applications, many=True)
            for application_data in serializer.data:
                user_id = application_data['user'] 
                user = Users.objects.get(pk=user_id) 
                user_data = {'user_id': user.user_id, 'name': user.name, 'email': user.email}
                application_data['user'] = user_data 
                job_id = application_data['job'] 
                job = Job.objects.get(pk=job_id) 
                job_data = {'job_id': job.job_id, 'job_title': job.job_title, 'job_url': job.job_url, 'company': {'company_id': job.company.company_id, 'company_name': job.company.company_name, 'company_description': job.company.company_description}, 'job_location': job.job_location, 'job_description': job.job_description}
                application_data['job'] = job_data 
            return Response(serializer.data)

    def post(self, request):
        serializer = ApplicationsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            application = Applications.objects.get(pk=pk)
        except Applications.DoesNotExist:
            raise Http404

        serializer = ApplicationsSerializer(application, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            application = Applications.objects.get(pk=pk)
        except Applications.DoesNotExist:
            raise Http404

        application.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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
    
class ApplicationCompareAPIView(APIView):
     def post(self, request):
        job_description_id = request.data.get('job_description_id')
        resume_file = request.FILES.get('resume')

        if not job_description_id or not resume_file:
            return Response({'error': 'Please provide job description ID and resume file'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            job_description = Applications.objects.get(pk=job_description_id)
        except Applications.DoesNotExist:
            return Response({'error': 'Job description with the provided ID does not exist'}, status=status.HTTP_404_NOT_FOUND)

        default_user, _ = Users.objects.get_or_create(name='John Doe')
        resume = Resume(user=default_user, file=resume_file, id=1)
        resume.save()

        missing_words = self.compare_texts(job_description.job_description, resume.file)

        return Response({'missing_words': missing_words})


     def compare_texts(self, job_description_text, resume):
        job_description_text = set(job_description_text.lower().split())
        resume_text = set(resume.read().lower().split())

        missing_words = list(job_description_text - resume_text)

        return missing_words