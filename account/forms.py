from django import forms 
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from .models import Create_User

class CostumUserCreationForm(UserCreationForm):
    class Meta:
        model=Create_User
        fields=("username","email","first_name","last_name","Age","Address")

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Create_User
        fields=("username","email","first_name","last_name","Age","Address")
# authentication/forms.py

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)