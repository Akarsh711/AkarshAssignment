from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Task, CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Fields displayed in the admin panel
    list_display = ("username", "phone_number", "email", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")

    # Define fieldsets for user editing
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (("Personal info"), {"fields": ("email", "phone_number")}),
        (("Permissions"), {"fields": ("is_staff", "is_superuser", "is_active")}),
    )

    # Define fields for adding a new user
    add_fieldsets = (
        (None, {"fields": ("username", "password1", "password2", "phone_number", "is_staff", "is_active"), }),
    )

    search_fields = ("username", "email", "phone_number")
    ordering = ("username",)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Task)
