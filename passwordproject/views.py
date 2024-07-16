from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ResetPinSerializer
from django.contrib.auth.models import User

class ResetPinRequestView(APIView):
    def post(self, request):
        serializer = ResetPinSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            user = User.objects.get(email=email)
            # Send email with pin reset instructions
            # For testing, this will print to the console
            print(f"Send pin reset instructions to {email}")
            return Response({"message": "Pin reset instructions sent"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.

