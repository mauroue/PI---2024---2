from django import forms
from app.models.documents import Documents


class DocumentUploadForm(forms.ModelForm):
    crea_file = forms.FileField(required=False)
    passport_file = forms.FileField(required=False)
    cpf_file = forms.FileField(required=False)
    rg_file = forms.FileField(required=False)

    class Meta:
        model = Documents
        fields = []
