from django.urls import path
from hospitals import views
urlpatterns = [
    path('doctor/register/', views.doctor_register, name="doctor_register"),
    path("doctor/list/", views.doctor_list, name="doctor_list"),
    path("doctor/<int:doctor_id>/appointments/", views.doctor_appointments, name="doctor_appointments"),
    path("appointment/list/", views.appointment_list, name="appointment_list"),
    path("appointment/create/", views.appointment_create, name="appointment_create"),
    path("appointment/<int:appointment_id>/delete/", views.appointment_delete, name="appointment_delete"),
    path("appointment/<int:appointment_id>/book/", views.appointment_book, name="appointment_book"),
]