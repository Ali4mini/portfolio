from django.contrib import admin

from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    # What you see in the list
    list_display = ("name", "email", "subject", "created_at", "is_read")
    # Filter by date or read status
    list_filter = ("is_read", "created_at")
    # Make fields read-only so you don't accidentally edit a client's message
    readonly_fields = ("name", "email", "subject", "message", "created_at")

    # Organize the detail view
    fieldsets = (
        ("Client Info", {"fields": ("name", "email")}),
        ("Message Content", {"fields": ("subject", "message", "created_at")}),
        ("Status", {"fields": ("is_read",)}),
    )
