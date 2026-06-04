from django.contrib import admin
from .models import User
from django.utils.html import format_html

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "bio", "created_at", "is_staff", "is_superuser", "image_path")

    @admin.display(description="Profile Pics")
    def image_path(self, obj):
        if obj.profile_picture:
            return format_html(
                "<img src='{}' width='50px' height='50px'>",
                obj.profile_picture.url
            )
        return "No Image"



