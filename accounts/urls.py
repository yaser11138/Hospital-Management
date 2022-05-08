from django.urls import path
from accounts.views import register, user_login, user_logout,ResetPasswordConfirm,ResetPassword
urlpatterns = [
    path('register/', register, name="register"),
    path('login/', user_login, name="login"),
    path('logout/', user_logout, name="logout"),
    path("reset/", ResetPassword.as_view(), name="password_reset"),
    path("reset/<uidb64>/<token>/", ResetPasswordConfirm.as_view(), name="password_reset_confirm"),
]