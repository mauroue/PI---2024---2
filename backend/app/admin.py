from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app.forms.custom_user import AppUserCreationForm, UserChangeForm
from app.models.app_user import AppUser

class AppUserAdmin(UserAdmin):
    add_form = AppUserCreationForm
    form = UserChangeForm
    model = AppUser
    list_display = ["name", "dob",
                  "cpf", "rg"]

admin.site.register(AppUser, AppUserAdmin)
