from .models import Like
from rest_framework import serializers


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model=Like
        fields=["id", "post", "user", "created_at"]
        read_only_fields=["id", "user", "created_at"]