from django.shortcuts import render, redirect, reverse
from accounts.forms import UserRegistration
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.contrib.messages.views import SuccessMessageMixin


def register(request):
    if request.method == "POST":
        user = UserRegistration(data=request.POST)
        if user.is_valid():
            user = user.save()
            login(request, user)
            if request.POST.get("type_choices") == 'D':
                return redirect(reverse("doctor"))
            return redirect(reverse("appointment_list"))
        else:
            return render(request, "register.html", {"form": user})
    else:
        user = UserRegistration()
        return render(request, "register.html", {"form": user})


def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect(reverse("appointment_list"))
        else:
            return render(request, "login.html", {"error": "the username or password is invalid"})
    else:
        return render(request, "login.html")


@login_required(login_url='/accounts/login/')
def user_logout(request):
    logout(request)
    return redirect(reverse("login"))


class ResetPassword(SuccessMessageMixin, PasswordResetView):
    template_name = "password-reset.html"
    success_url = reverse_lazy('login')
    success_message = "a Email is sent to your email address"


class ResetPasswordConfirm(SuccessMessageMixin, PasswordResetConfirmView):
    template_name = "password-reset-confirm.html"
    success_url = reverse_lazy('login')
    SuccessMessageMixin = "your password is changed successfully"
