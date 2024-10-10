import uuid
from app.models.profile import Profile
from django.contrib.auth.models import AbstractUser, BaseUserManager
from app.validators import validate_cpf
from django.db import models
from django.conf import settings

DEFAULT_PROFILE_IMAGE = "static/images/default_profile.jpg"

STATUS_CHOICES = [
    ("new", "Novo"),
    ("pending_documentation", "Aguardando Documentação"),
    ("pending_aproval", "Aguardando Aprovação"),
    ("suspended", "Suspenso"),
    ("banned", "Banido"),
    ("able", "Apto"),
]


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, username, password, **extra_fields)


def user_directory_path(instance, filename):
    unique_filename = f"{uuid.uuid4()}{filename[filename.rfind('.'):]}"
    return f"user_{instance.id}/{unique_filename}"


class User(AbstractUser):
    name = models.CharField(max_length=100)
    dob = models.DateField(null=True)
    crea = models.CharField(max_length=100, null=True)
    active = models.BooleanField(default=True)
    passport_due = models.DateField(null=True)
    cpf = models.CharField(
        max_length=11, blank=False, null=False, unique=True, validators=[validate_cpf]
    )
    rg = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=100, unique=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="new")
    is_worker = models.BooleanField(default=True)
    profile_image = models.FileField(
        upload_to=user_directory_path,
        null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "dob", "cpf"]

    def save(self):
        super(User, self).save()
        profile = Profile.objects.filter(user=self)
        if profile:
            print("ok")


    def __str__(self):
        return self.name or self.username or "Anônimo"
