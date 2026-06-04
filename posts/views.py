from .models import Post
from .serializers import PostSerializer
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from config.permissions import IsAuthorOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import MultiPartParser, FormParser


class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.select_related("user").all().order_by("created_at")
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    # parser_classes = [MultiPartParser, FormParser]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields= ["title"]
    search_fields = ["title", "contents"]
    ordering_fields = ["created_at"]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)