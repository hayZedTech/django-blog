from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("texts", "post", "user", "created_at")
    search_fields = ("texts", "post",)
    list_filter = ("created_at", "user")
    ordering = ("-created_at",)


