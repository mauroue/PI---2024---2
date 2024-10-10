from django import forms


class DocumentUploadForm(forms.Form):
    crea_file = forms.FileField(label="CREA", required=False)
    passport_file = forms.FileField(label="Passaporte", required=False)
    cpf_file = forms.FileField(label="CPF", required=False)
    rg_file = forms.FileField(label="RG", required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})
