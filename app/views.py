from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from app.forms.register import UserRegistrationForm
from app.forms.update_user_info import UserUpdateForm
from django.contrib.auth.decorators import login_required
from app.forms.work_request_form import WorkRequestForm
from app.models.documents import Documents
from app.models.work_requests import WorkRequest
from app.models.work_user_proposals import WorkUserProposal
from django.contrib.auth import login
from app.models.files import Files
import logging

logger = logging.getLogger(__name__)


@login_required
def update_user_info(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, "dashboard/user/update_user_info.html", {"form": form})


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
    return redirect("list_work_request")


def register_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("user_dashboard")
    else:
        form = UserRegistrationForm()

    return render(request, "registration/register.html", {"form": form})


@login_required
def user_profile(request):
    if request.method == "POST" and request.FILES.get("profile_image"):
        user = request.user
        user.profile_image = request.FILES.get("profile_image")
        print(user.profile_image)
        user.save()
        return redirect("user_profile")

    user_files = Files.objects.filter(user=request.user)
    profile_image = (
        request.user.profile_image.url if request.user.profile_image else None
    )
    print(profile_image)
    return render(
        request,
        "dashboard/user/profile.html",
        {"user_files": user_files, "profile_image": profile_image},
    )


@login_required
def upload_file(request):
    if request.method == "POST":
        print(request)
        document_types = ["crea", "passport", "cpf", "rg"]
        for doc_type in document_types:
            file = request.FILES.get(f"{doc_type}_file")
            if file:
                # Create a new Files instance
                file_instance = Files.objects.create(
                    user=request.user, upload_to=file, doc_type=doc_type
                )

                # Get or create a Documents instance for the user
                documents, _ = Documents.objects.get_or_create(user=request.user)

                # Update the corresponding field in Documents
                setattr(documents, doc_type, file_instance)
                documents.save()

        messages.success(request, "Documentos enviados com sucesso!")
        return redirect("user_profile")

    return render(request, "dashboard/user/upload_file.html")
