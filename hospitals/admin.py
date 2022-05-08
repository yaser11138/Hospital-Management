from django.contrib import admin
from .models import Appointment, Doctor


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    fields = ("doctor", "patient", "date", "time")


@admin.register(Doctor)
class AppointmentAdmin(admin.ModelAdmin):
    fields = ("user", "expertise",)