from .models import Comment
from .serializers import CommentSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from config.permissions import IsAuthorOrReadOnly


class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.select_related("user", "post").all().order_by("created_at")
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)