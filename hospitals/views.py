from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from hospitals.models import Doctor, Appointment
from .forms import AppointmentForm
from django.contrib.auth import get_user_model
from .decorators import doctor_login_required
from django.contrib.auth.decorators import login_required
User = get_user_model()


def doctor_register(request):
    if request.POST:
        expertise = request.POST.get("expertise")
        description = request.POST.get("description")
        Doctor.objects.create(user=request.user, expertise=expertise, description=description)
        return redirect(reverse("appointment_list"))
    else:
        return render(request, "doctor_register.html")


@login_required(login_url=reverse_lazy("login"))
def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, "doctor_list.html", {"doctors": doctors})


# get the doctor appointments
@login_required(login_url=reverse_lazy("login"))
def doctor_appointments(request, doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    appointments = Appointment.objects.filter(doctor=doctor,patient=None)
    context = {"appointments": appointments}
    return render(request, "doctor_appointments.html", context)


# get the user appointments
@login_required(login_url=reverse_lazy("login"))
def appointment_list(request):
    appointments = Appointment.objects.related_appointment_to_user(user=request.user)
    context = {"appointments": appointments}
    return render(request, "appointment_list.html", context)


@doctor_login_required
def appointment_create(request):
    if request.method == "POST":
        appointment = AppointmentForm(request.POST)
        if appointment.is_valid():
            appointment = appointment.save(commit=False)
            appointment.doctor = request.user.doctor
            appointment.save()
            return redirect(reverse("appointment_list"))
        else:
            return render(request, "appointments_create.html", {'errors': appointment.errors})

    else:
        appointment_form = AppointmentForm()
        return render(request, "appointments_create.html", {"form": appointment_form})


@login_required(login_url=reverse_lazy("login"))
def appointment_book(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    appointment.patient = request.user
    appointment.save()
    return redirect(reverse("appointment_list"))


@login_required(login_url=reverse_lazy("login"))
def appointment_delete(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    if request.user.is_doctor:
        appointment.delete()
    else:
        appointment.patient = None
        appointment.save()
    return redirect("appointment_list")