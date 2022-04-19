def doctor_login_required(user):
        if user.is_doctor and user.is_authenticated:
            return True
        else:
            return False
