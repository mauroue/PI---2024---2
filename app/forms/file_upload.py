from django import forms
from app.models.files import Files


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ["upload_to"]
