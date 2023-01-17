from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CostumUserCreationForm,CustomUserChangeForm
from.models import Create_User

class CostumUserAdmin(UserAdmin):
    add_form = CostumUserCreationForm
    form = CustomUserChangeForm
    model = Create_User
    list_display = ["email", "username","first_name","last_name","Age","Address"]

admin.site.register(Create_User, CostumUserAdmin)