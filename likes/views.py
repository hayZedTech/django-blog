from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Like
from .serializers import LikeSerializer


class LikeViewset(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]


    def create(self, request, *args, **kwargs):
        post_id = request.data.get("post")
        user = request.user

        is_liked = Like.objects.filter(user=user, post_id=post_id)

        if is_liked.exists():
            is_liked.delete()
            return Response({"message":"Post unliked successfully!"})
        return super().create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
