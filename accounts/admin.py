from django.contrib import admin
from .models import User


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ("username",)
    fields = ("username", "password", "email", "phone", "address", "gender", "age")

