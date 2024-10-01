import uuid
from django.conf import settings
from django.db import models
from app.models.users import User


def user_directory_path(instance, filename):
    unique_filename = f"{uuid.uuid4()}{filename[filename.rfind('.'):]}"
    return f"user_{instance.user.id}/{unique_filename}"


class Files(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile_image"
    )
    upload_to = models.FileField(upload_to=user_directory_path)
    secure = models.BooleanField(default=False)
    lgpd = models.BooleanField(default=False)
    doc_type = models.CharField(max_length=30, default="other")
