from django import forms
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from app.models.users import User


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(label="Email", max_length=200, help_text="Obrigatório.")
    name = forms.CharField(
        max_length=100, label="Nome Completo", required=True, help_text="Obrigatório."
    )
    dob = forms.DateField(
        required=True,
        label="Data de nascimento",
        help_text="Obrigatório. Deve ser uma data válida.",
        widget=forms.SelectDateWidget(years=range(1925, 2025)),
    )
    cpf = forms.CharField(
        max_length=11,
        required=True,
        label="CPF",
        error_messages={"required": "Este campo é obrigatório."},
    )

    class Meta:
        model = User
        fields = ("email", "password1", "password2", "name", "dob", "cpf")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.fields.get("username"):
            del self.fields["username"]

        self.helper = FormHelper()
        self.helper.add_input(
            Submit("submit", "Registrar", css_class="btn btn-primary")
        )
