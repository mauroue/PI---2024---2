from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from app.forms.register import UserRegistrationForm
from app.forms.update_user_info import UserUpdateForm
from django.contrib.auth.decorators import login_required

class RegisterView(CreateView):
    form_class = UserRegistrationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy('login')

@login_required
def update_user_info(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to the dashboard or another page
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'dashboard.html', {'form': form})