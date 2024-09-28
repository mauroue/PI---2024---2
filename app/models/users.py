from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


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


class User(AbstractUser):
    name = models.CharField(max_length=100, blank=True)
    dob = models.DateField(null=True, blank=True)
    crea = models.CharField(max_length=100, blank=True, null=True)
    active = models.BooleanField(default=True)
    passport_due = models.DateField(blank=True, null=True)
    cpf = models.CharField(max_length=11, blank=False, null=False, unique=True)
    rg = models.CharField(max_length=20, null=False, blank=False)
    email = models.CharField(max_length=100, unique=True)
    visa = models.ForeignKey(
        "Visa", on_delete=models.SET_NULL, null=True, related_name="users"
    )
    address = models.ForeignKey(
        "Address", on_delete=models.SET_NULL, null=True, related_name="users"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "dob"]

    def user_directory_path(self, filename):
        return f"media/user_storage/user_{self.pk}/{filename}"

    def __str__(self):
        return self.name or self.username
