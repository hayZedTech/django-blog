from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import LikeViewset


router = DefaultRouter()
router.register(r"", LikeViewset, basename="likes")

urlpatterns=router.urls