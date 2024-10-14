"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from app import views
from app.views import (
    apply_work_request,
    register_view,
    list_work_request,
    cancel_work_request,
    upload_file,
    user_profile,
    admin_document_dashboard,
)
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic.base import TemplateView
from app.views import create_work_request
from django.conf.urls.static import static

urlpatterns = [
    # Admin URLs
    path(
        "admin/document-dashboard/",
        admin_document_dashboard,
        name="admin_document_dashboard",
    ),
    path("admin/", admin.site.urls),
    # Views
    path("register/", register_view, name="register"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path(
        "password_change/",
        auth_views.PasswordChangeView.as_view(
            template_name="registration/password_change_form.html"
        ),
        name="password_change",
    ),
    path(
        "password_change/done/",
        auth_views.PasswordChangeDoneView.as_view(
            template_name="registration/password_change_done.html"
        ),
        name="password_change_done",
    ),
    # templates
    path("", TemplateView.as_view(template_name="index.html"), name="index"),
    path(
        "dashboard/",
        TemplateView.as_view(template_name="dashboard/home.html"),
        name="user_dashboard",
    ),
    path("work_requests/", list_work_request, name="list_work_request"),
    path("work_requests/new/", create_work_request, name="create_work_request"),
    path(
        "work_requests/<int:pk>/cancel/",
        cancel_work_request,
        name="cancel_work_request",
    ),
    path(
        "work_requests/<int:pk>/apply/", apply_work_request, name="apply_work_request"
    ),
    path("profile/", user_profile, name="user_profile"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path("upload-file/", upload_file, name="upload_file"),
    path(
        "create-proposal/<int:work_request_id>/",
        views.create_proposal_form,
        name="create_proposal_form",
    ),
    path(
        "submit-proposal/<int:work_request_id>/",
        views.submit_proposal,
        name="submit_proposal",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
