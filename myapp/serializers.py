from rest_framework import serializers
from django.contrib.auth.models import User

class ResetPinSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email address not found")
        return value
