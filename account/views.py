from django.shortcuts import render,redirect
from .forms import CostumUserCreationForm,LoginForm
from django.contrib import messages
from django.contrib.auth import login, authenticate #
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from django.views.decorators.csrf import csrf_exempt
from . import forms
@csrf_exempt
def home(request):
    return render(request,'account/home.html')
@csrf_exempt
def SignUp(request):
    if request.method == 'POST':
        form = CostumUserCreationForm(request.POST)
        if form.is_valid():
            print('data',form.cleaned_data)
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return render(request,'account/login.html')
    else:
        form = CostumUserCreationForm()

    context = {'form': form}
    return render(request, 'account/signup.html', context)

@csrf_exempt
def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'Hello {user.username}! You have been logged in'
                return render(request,'account/after_login.html')
                
            else:
                message = 'Login failed!'
    return render(request, 'account/login.html', context={'form': form, 'message': message})