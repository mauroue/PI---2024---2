from django import forms
from app.models.documents import Documents


class DocumentUploadForm(forms.ModelForm):
    crea = forms.FileField(
        required=False, widget=forms.FileInput(attrs={"class": "form-control"})
    )
    passport = forms.FileField(
        required=False, widget=forms.FileInput(attrs={"class": "form-control"})
    )
    cpf = forms.FileField(
        required=False, widget=forms.FileInput(attrs={"class": "form-control"})
    )
    rg = forms.FileField(
        required=False, widget=forms.FileInput(attrs={"class": "form-control"})
    )

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
            "crea",
            "crea_number",
            "passport",
            "passport_number",
            "cpf",
            "cpf_number",
            "rg",
            "rg_number",
        ]
