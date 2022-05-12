from django.contrib import admin
from accounts.models import CustomUser, Language, UserType
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
# Register your models here.
admin.site.register([UserType, Language])

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        'email', 'username', 'user_type', 'preferred_language', 'is_staff'
    ]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('user_type', 'preferred_language')}),
        )
    add_field_sets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('user_type', 'preferred_language')}),
        )

admin.site.register(CustomUser, CustomUserAdmin)
