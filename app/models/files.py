import uuid
from django.db import models
from app.models.users import User


def user_directory_path(instance, filename):
    unique_filename = f"{uuid.uuid4()}{filename[filename.rfind('.'):]}"
    return f"user_{instance.user.id}/{unique_filename}"


class Files(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_to = models.FileField(upload_to=user_directory_path)
    secure = models.BooleanField(default=False)
    lgpd = models.BooleanField(default=False)
