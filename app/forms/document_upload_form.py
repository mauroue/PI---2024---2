from django import forms
from app.models.documents import Documents


class DocumentUploadForm(forms.ModelForm):
    crea_number = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Número do CREA"}
        ),
    )
    passport_number = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Número do Passaporte"}
        ),
    )
    cpf_number = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Número do CPF"}
        ),
    )
    rg_number = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Número do RG"}
        ),
    )

    class Meta:
        model = Documents
        fields = [
            "crea_number",
            "passport_number",
            "cpf_number",
            "rg_number",
        ]
