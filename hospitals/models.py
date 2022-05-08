from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
user = get_user_model()


class Doctor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    expertise = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.user.username}"


class AppointmentManager(models.Manager):

    def related_appointment_to_user(self, user):
        if user.is_doctor:
            appointments = Appointment.objects.filter(doctor=user.doctor)
        else:
            appointments = Appointment.objects.filter(patient=user)
        return appointments


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(user, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    time = models.TimeField()
    objects = AppointmentManager()

    class Meta:
        unique_together = ["date", "time"]

    def __str__(self):
        return self.description
