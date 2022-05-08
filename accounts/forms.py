from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
import re
user = get_user_model()


class UserRegistration(UserCreationForm):
    TYPES = (
        ("P", "Patient"),
        ("D", "Doctor"),
    )
    type_choices = forms.ChoiceField(choices=TYPES)

    class Meta:
        model = user
        fields = ("username", "phone", "address", "gender", "age", "email", "first_name", "last_name",)

    def clean_phone(self):
        phone = self.cleaned_data["phone"]
        regex = r'^09\d{9}$'
        x = re.fullmatch(regex, phone)
        if bool(x) is False:
            raise forms.ValidationError('Enter a valid mobile number. This value may contain numbers only,'
                                        'and must be exactly 11 digits starting with "09"')
        else:
            return phone

    def clean_email(self):
        email = self.cleaned_data["email"]
        if user.objects.filter(email=email):
            raise forms.ValidationError("this email address is already used")
        else:
            return email
