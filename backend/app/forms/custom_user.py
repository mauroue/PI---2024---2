from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from app.models.app_user import AppUser


class AppUserCreationForm(UserCreationForm):

    class Meta:
        model = AppUser
        fields = ("name", "dob",
                  "cpf", "rg")

class AppUserChangeForm(UserChangeForm):

    class Meta:
        model = AppUser
        fields = ("name", "dob",
                  "cpf", "rg")
