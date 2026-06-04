from .models import Post
from rest_framework import serializers
from accounts.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    likes_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model=Post
        fields=["id", "title", "contents", "user", "likes_count", "comments_count", "image", "created_at", "updated_at"]
        read_only_fields=["id", "user", "created_at", "updated_at"]


    def get_likes_count(self, obj):
        return obj.likes.count()
    
    def get_comments_count(self, obj):
        return obj.comments.count()