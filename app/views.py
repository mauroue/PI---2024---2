from django.urls import reverse_lazy
from django.views.generic import CreateView
from app.forms.register import UserRegistrationForm

class RegisterView(CreateView):
    form_class = UserRegistrationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy('login')
