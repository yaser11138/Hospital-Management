from django.contrib.auth.decorators import user_passes_test

def doctor_login_required(func):
    def is_doctor_login(user):
        if user.is_doctor and user.is_authenticated:
            return True
        else:
            return False
    decorator = user_passes_test(is_doctor_login)
    return decorator(func)
