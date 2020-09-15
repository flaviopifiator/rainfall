from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from rainfall.core.admin import SingletonAdmin


User = get_user_model()


@admin.register(User)
class UserAdmin(SingletonAdmin, auth_admin.UserAdmin):
    pass
