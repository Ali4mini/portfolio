from django.contrib import admin

from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title_en", "category", "is_featured", "created_at")
    list_filter = ("category", "is_featured")
    search_fields = ("title_en", "title_fa", "tools")
    prepopulated_fields = {"slug": ("title_en",)}

    fieldsets = (
        (
            "Settings",
            {
                "fields": (
                    "slug",
                    "is_featured",
                    "category",
                    "image",
                    "tools",
                    "github_url",
                    "live_url",
                )
            },
        ),
        ("English Content", {"fields": ("title_en", "description_en", "body_en")}),
        (
            "Persian Content",
            {
                "classes": ("collapse",),  # Click to expand (keeps UI clean)
                "fields": ("title_fa", "description_fa", "body_fa"),
            },
        ),
    )
