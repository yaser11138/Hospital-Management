from django import forms
from django.core.exceptions import NON_FIELD_ERRORS
from .models import Appointment
import datetime


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ("date", "time",)
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }

    def clean(self):
        if self.cleaned_data["date"] < datetime.date.today():
            raise forms.ValidationError("the date cannot be in past")
        elif self.cleaned_data["date"] == datetime.date.today() and self.cleaned_data["time"] < datetime.datetime.now().time():
            raise forms.ValidationError("the time cannot be in past")
        return self.cleaned_data
