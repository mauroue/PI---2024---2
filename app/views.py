from django.shortcuts import get_object_or_404, redirect, render
from app.forms.register import UserRegistrationForm
from app.forms.update_user_info import UserUpdateForm
from django.contrib.auth.decorators import login_required
from app.forms.work_request_form import WorkRequestForm
from app.models.work_requests import WorkRequest
from app.models.work_user_proposals import WorkUserProposal
from django.contrib.auth import login


@login_required
def update_user_info(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, "dashboard.html", {"form": form})


@login_required
def create_work_request(request):
    if request.method == "POST":
        form = WorkRequestForm(request.POST)
        if form.is_valid():
            work_request = form.save(commit=False)
            work_request.requester = request.user
            work_request.save()
            return redirect("list_work_request")
    else:
        form = WorkRequestForm()
    return render(request, "requests/work_request_create.html", {"form": form})


@login_required
def list_work_request(request):
    work_requests = WorkRequest.objects.all()
    return render(
        request, "requests/work_request_list.html", {"work_requests": work_requests}
    )


@login_required
def cancel_work_request(request, pk):
    work_request = get_object_or_404(WorkRequest, pk=pk, requester=request.user)
    if request.method == "POST":
        work_request.status = "cancelled"
        work_request.save()
    return redirect("list_work_request")


@login_required
def apply_work_request(request, pk):
    work_request = get_object_or_404(WorkRequest, pk=pk)
    if request.method == "POST":
        # Create a new WorkUserProposal instance
        WorkUserProposal.objects.create(
            work_request=work_request,
            user=request.user,
            proposal_text="Application for the work request.",
        )
    return redirect("work_request_list")


def register_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserRegistrationForm()

    return render(request, "registration/register.html", {"form": form})
