from django.contrib import admin
from .models import Post
from django.utils.html import format_html


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "created_at", "image_path")
    search_fields = ("title", "contents")
    list_filter = ("created_at", "user")
    ordering = ("-created_at",)

    @admin.display(description="images")
    def image_path(self, obj):
        if obj.image:
            return format_html(
                "<img src='{}' width='50px' height='50px'>",
                obj.image.url
            )
        return "No Image"

