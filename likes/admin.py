from django.contrib import admin
from .models import Like


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("post", "user", "created_at")
    search_fields = ("post_title",)
    list_filter = ("created_at", "user")
    ordering = ("-created_at",)


