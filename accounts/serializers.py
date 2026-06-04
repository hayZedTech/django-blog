from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id", "username",  "email", "profile_picture", "bio", "created_at"]


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields=["id", "username", "password", "email", "profile_picture", "bio", "created_at"]
        read_only_fields=["id", "created_at"]


    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user