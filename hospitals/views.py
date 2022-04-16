from django.shortcuts import render, redirect
from django.urls import reverse
from hospitals.models import Doctor, Appointment
from .forms import AppointmentForm
from django.contrib.auth import get_user_model
user = get_user_model()


def doctor_register(request):
    if request.POST:
        expertise = request.POST.get("expertise")
        description = request.POST.get("description")
        Doctor.objects.create(user=request.user, expertise=expertise, description=description)
        return redirect(reverse("appointment_list"))
    else:
        return render(request, "doctor.html")


def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, "doctor_list.html", {"doctors": doctors})


def doctor_appointments(request, doctor_id):
    doctor = user.objects.get(doctor__id=doctor_id)
    appointments = Appointment.objects.related_appointment_to_user(user=doctor)
    context = {"appointments": appointments}
    return render(request, "doctor_appointments.html", context)


def appointment_list(request):
    appointments = Appointment.objects.related_appointment_to_user(user=request.user)
    context = {"appointments": appointments}
    return render(request, "appointment_list.html", context)


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
        appointment = AppointmentForm()
        return render(request, "appointments_create.html", {"form": appointment})


def appointment_book(request,appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    appointment.patient = request.user
    appointment.save()
    return redirect(reverse("appointment_list"))
