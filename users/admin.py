from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model


from users.models import CustomUser
User = get_user_model()


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username','email','is_staff']

admin.site.register(CustomUser, CustomUserAdmin)