from django import forms
from app.models.address import Address
from app.models.contact_info import ContactInfo


class PersonalInfoForm(forms.Form):
    # Contact Information
    phone = forms.CharField(
        max_length=13,
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    phone_alt = forms.CharField(
        max_length=13,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    # Address Information
    address = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    zipcode = forms.CharField(
        max_length=8,
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    city = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    state = forms.CharField(
        max_length=2,
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    def save(self, user):
        address = Address.objects.create(
            user=user,
            address=self.cleaned_data["address"],
            zipcode=self.cleaned_data["zipcode"],
            city=self.cleaned_data["city"],
            state=self.cleaned_data["state"],
        )

        contact_info = ContactInfo.objects.create(
            user=user,
            phone=self.cleaned_data["phone"],
            phone_alt=self.cleaned_data["phone_alt"],
        )

        return address, contact_info
