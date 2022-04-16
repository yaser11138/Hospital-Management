from django.urls import path
from hospitals import views
urlpatterns = [
    path('doctorregister/', views.doctor_register, name="doctor_register"),
    path("appointmentlist/", views.appointment_list, name="appointment_list"),
    path("appointmentcreate/", views.appointment_create, name="appointment_create"),
    path("doctors/", views.doctor_list, name="doctor_list"),
    path("doctor/<int:doctor_id>/tasks/",views.doctor_appointments, name="doctor_appointments"),
    path("task/<int:appointment_id>/book/",views.appointment_book, name="appointment_book")


]