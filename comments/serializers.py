from .models import Comment
from rest_framework import serializers
from accounts.serializers import UserSerializer


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model=Comment
        fields=["id", "texts", "post", "user", "created_at", "updated_at"]
        read_only_fields=["id", "user", "created_at", "updated_at"]