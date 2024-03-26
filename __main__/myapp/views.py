from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserDetails
from .serializers import UserDetailsSerializer  # Importing serializer

class UserDetailsAPIView(APIView):
    def get(self, request):
        userDetails = UserDetails.objects.all()
        serializer = UserDetailsSerializer(userDetails, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        userDetails = UserDetails.objects.get(pk=pk)
        serializer = UserDetailsSerializer(userDetails, data=request.data)
        if serializer.is_valid():
            serializer.save()   
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)