from django import forms
from app.models.work_requests import WorkRequest


class WorkRequestForm(forms.ModelForm):
    class Meta:
        model = WorkRequest
        fields = ["title", "description", "budget"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "budget": forms.NumberInput(attrs={"class": "form-control"}),
        }
