from django.contrib import admin

from .models import Project

# Register your models here.


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "is_featured", "created_at", "tools")
    list_filter = ("is_featured", "created_at")
