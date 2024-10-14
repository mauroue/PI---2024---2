from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from app.forms.document_upload_form import DocumentUploadForm
from app.forms.register import UserRegistrationForm
from app.forms.update_user_info import UserUpdateForm
from django.contrib.auth.decorators import login_required
from app.forms.work_request_form import WorkRequestForm
from app.models.documents import Documents
from app.models.profile import Profile
from app.models.work_requests import WorkRequest
from app.models.work_user_proposals import WorkUserProposal
from django.contrib.auth import login
from app.models.files import Files
import logging
from django.contrib.admin.views.decorators import staff_member_required
from .forms.work_user_proposal_form import WorkUserProposalForm

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
        profile_image = request.FILES["profile_image"]
        request.user.profile_image = profile_image
        request.user.save()
        return redirect("user_profile")

    user_files = Files.objects.filter(user=request.user)
    documents, created = Documents.objects.get_or_create(user=request.user)
    profile_image = (
        request.user.profile_image.url if request.user.profile_image else None
    )
    done = """<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor"
        class="bi bi-cloud-check-fill" viewBox="0 0 16 16">
        <path
            d="M8 2a5.53 5.53 0 0 0-3.594 1.342c-.766.66-1.321 1.52-1.464 2.383C1.266 6.095 0 7.555 0 9.318 0 11.366 1.708 13 3.781 13h8.906C14.502 13 16 11.57 16 9.773c0-1.636-1.242-2.969-2.834-3.194C12.923 3.999 10.69 2 8 2m2.354 4.854-3 3a.5.5 0 0 1-.708 0l-1.5-1.5a.5.5 0 1 1 .708-.708L7 8.793l2.646-2.647a.5.5 0 0 1 .708.708" />
    </svg>
    """
    pending = """
    <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" class="bi bi-cloud-arrow-up-fill" viewBox="0 0 16 16">
  <path d="M8 2a5.53 5.53 0 0 0-3.594 1.342c-.766.66-1.321 1.52-1.464 2.383C1.266 6.095 0 7.555 0 9.318 0 11.366 1.708 13 3.781 13h8.906C14.502 13 16 11.57 16 9.773c0-1.636-1.242-2.969-2.834-3.194C12.923 3.999 10.69 2 8 2m2.354 5.146a.5.5 0 0 1-.708.708L8.5 6.707V10.5a.5.5 0 0 1-1 0V6.707L6.354 7.854a.5.5 0 1 1-.708-.708l2-2a.5.5 0 0 1 .708 0z"/>
</svg>
"""

    return render(
        request,
        "dashboard/user/profile.html",
        {
            "user_files": user_files,
            "profile_image": profile_image,
            "documents": documents,
            "done": done,
            "pending": pending,
        },
    )


@login_required
def upload_file(request):
    documents, created = Documents.objects.get_or_create(user=request.user)
    documents_uploaded = {
        "crea_file": documents.crea is not None,
        "passport_file": documents.passport is not None,
        "cpf_file": documents.cpf is not None,
        "rg_file": documents.rg is not None,
    }

    if request.method == "POST":
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            for field_name in ["crea", "passport", "cpf", "rg"]:
                file = form.cleaned_data.get(f"{field_name}_file")
                if file and not documents_uploaded[f"{field_name}_file"]:
                    file_instance = Files.objects.create(
                        user=request.user, upload_to=file, doc_type=field_name
                    )
                    setattr(documents, field_name, file_instance)

            documents.save()
            messages.success(request, "Documentos enviados com sucesso!")
            return redirect("user_profile")
    else:
        form = DocumentUploadForm()

    return render(
        request,
        "dashboard/user/upload_file.html",
        {"form": form, "documents_uploaded": documents_uploaded},
    )


@staff_member_required
def admin_document_dashboard(request):
    users_with_complete_docs = Profile.objects.filter(
        user__documents__crea__isnull=False,
        user__documents__passport__isnull=False,
        user__documents__cpf__isnull=False,
        user__documents__rg__isnull=False,
    ).select_related("user", "user__documents")

    return render(request, "admin/dashboard.html", {"users": users_with_complete_docs})


def create_proposal(request, work_request_id):
    work_request = WorkRequest.objects.get(id=work_request_id)
    if request.method == "POST":
        form = WorkUserProposalForm(request.POST)
        if form.is_valid():
            proposal = form.save(commit=False)
            proposal.work_request = work_request
            proposal.user = request.user
            proposal.save()
            return redirect("work_request_detail", pk=work_request.id)
    else:
        form = WorkUserProposalForm()
    return render(
        request, "create_proposal.html", {"form": form, "work_request": work_request}
    )


def create_proposal_form(request, work_request_id):
    work_request = WorkRequest.objects.get(id=work_request_id)
    form = WorkUserProposalForm()
    return render(
        request,
        "requests/proposal_form.html",
        {"form": form, "work_request": work_request},
    )


def submit_proposal(request, work_request_id):
    if request.method == "POST":
        form = WorkUserProposalForm(request.POST)
        if form.is_valid():
            proposal = form.save(commit=False)
            proposal.work_request_id = work_request_id
            proposal.user = request.user
            proposal.save()
            return JsonResponse({"status": "success"})
    return JsonResponse({"status": "error"})
