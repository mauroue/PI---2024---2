from django import forms
from django.contrib.auth.forms import UserCreationForm
from app.models.users import User


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text="Required")
    name = forms.CharField(
        max_length=100, label="Nome Completo", required=True, help_text="Required"
    )
    dob = forms.DateField(
        required=True,
        label="Data de nascimento",
        widget=forms.SelectDateWidget(years=range(1900, 2025)),
    )
    cpf = forms.CharField(
        max_length=11,
        required=True,
        label="CPF",
        help_text="Required. Must be 11 digits.",
        error_messages={"required": "Este campo é obrigatório."},
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "name", "dob", "cpf")
