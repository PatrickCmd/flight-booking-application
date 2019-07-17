import re

from django.contrib.auth import authenticate

from rest_framework import serializers

from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    """Registration serializer requests and creates a new user"""

    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User

        fields = ['email', 'password', 'date_of_birth', 'token',
                  'first_name', 'middle_name', 'last_name', 'gender',
                  'location', 'phone', 'image']
    
    def validate(self, data):
        password = data.get('password', None)

        # Raise an exception if the  password is not alphanumeric
        if not re.match("(?=.*[a-z])(?=.*[A-Z])"
                        "(?=.*[0-9])(?=.*[^a-zA-Z0-9])", password) or len(password) < 8:
            raise serializers.ValidationError(
                {"password": "The password should have atleast 8 characters a"
                "lowercase, uppercase, number and a special character"}
            )
        return data
    
    def get_cleaned_data(self, validated_data):
        return validated_data

    def create(self, validated_data):
        self.cleaned_data = self.get_cleaned_data(validated_data)
        user = User.objects.create_user(**self.cleaned_data)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    first_name = serializers.CharField(max_length=255, read_only=True)
    middle_name = serializers.CharField(max_length=255, read_only=True)
    last_name = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in'
            )
        
        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )
        
        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found'
            )
        
        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated'
            )
        
        if not user.is_verified:
            raise serializers.ValidationError(
                'This user has not been verified yet. Please do visit your email and follow instructions'
            )
        
        return {
            'email': user.email,
            'first_name': user.first_name,
            'middle_name': user.middle_name,
            'last_name': user.last_name,
            'location': user.location,
            'phone': user.phone,
            'image': user.image,
            'token': user.token
        }


class UserSerializer(serializers.ModelSerializer):
    """Handles serialization and deserialization of USer objects."""
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User
        fields = ('email', 'username', 'password')
    
    def update(self, instance, validated_data):
        """Performs an update on a User"""
        password = validated_data.pop('password', None)
        
        for key, value in validated_data.items():
            setattr(instance, key, value)
        
        if password is not None:
            instance.set_password(password)
        
        instance.save()

        return instance
