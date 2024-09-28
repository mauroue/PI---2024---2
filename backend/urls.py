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
from app.views import (
    apply_work_request,
    register_view,
    update_user_info,
    list_work_request,
    cancel_work_request,
    user_profile,
)
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.views.generic.base import TemplateView
from app.views import create_work_request
from django.conf.urls.static import static

urlpatterns = [
    # url files
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    # views
    path("dashboard/update/", update_user_info, name="update_user_info"),
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
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
