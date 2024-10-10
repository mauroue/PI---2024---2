from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from app.models.profile import Profile
from app.models.documents import Documents
from app.models.files import Files

User = get_user_model()


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "Profile"


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)


# Only try to unregister if the User model is registered
if User in admin.site._registry:
    admin.site.unregister(User)

admin.site.register(User, UserAdmin)
admin.site.register(Documents)
admin.site.register(Files)
