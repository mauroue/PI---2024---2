from django import forms
from django.contrib.auth.forms import UserCreationForm
from app.models.users import User


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(label='Email', max_length=200, help_text="Required")
    name = forms.CharField(
        max_length=100, label="Nome Completo", required=True, help_text="Required"
    )
    dob = forms.DateField(
        required=True,
        label="Data de nascimento",
        widget=forms.SelectDateWidget(years=range(1925, 2025)),
    )
    cpf = forms.CharField(
        max_length=11,
        required=True,
        label="CPF",
        help_text="Obrigatório. Deve ter 11 dígitos.",
        error_messages={"required": "Este campo é obrigatório."},
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "name", "dob", "cpf")
