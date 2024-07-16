from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ResetPinSerializer
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
import random

class ResetPinRequestView(APIView):
    def post(self, request):
        serializer = ResetPinSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            user = User.objects.get(email=email)
            # Send email with pin reset instructions

            # Generate a new PIN (for example, a 4-digit number)
            new_pin = random.randint(1000, 9999)

            # Here, you would update the user's PIN in your database
            user.profile.pin = new_pin
            user.profile.save()

            # Send an email with the new PIN
            send_mail(
                'Your new PIN',
                f'Your new PIN is {new_pin}',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )

            return Response({"message": "Pin reset instructions sent"}, status=status.HTTP_200_OK)


            # For testing, this will print to the console
            print(f"Send pin reset instructions to {email}")
            return Response({"message": "Pin reset instructions sent"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.

