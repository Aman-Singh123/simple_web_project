from django.shortcuts import render
from .forms import CostumUserCreationForm,LoginForm
from django.contrib import messages
from django.contrib.auth import login, authenticate 
from django.views.decorators.csrf import csrf_exempt
from . import forms
from django.contrib.auth.models import User
from django.http import JsonResponse , Http404
import json
@csrf_exempt
def home(request):
    return render(request,'account/home.html')


@csrf_exempt
def SignUp(request):
    print(f"request {request}")
    form = CostumUserCreationForm(request.POST or None)
    if request.method == 'POST':
        print(f"request {request.body}")
        data_dict=json.loads(request.body.decode("utf-8"))
        print(f"request {data_dict} {request.body}")
        try :
            if form.is_valid():
                form.save()
        except User.unique_error_message :
            raise Http404("account already exits")
        return JsonResponse({"success":True})
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
                print('data',form.cleaned_data)
                return render(request,'account/after_login.html') 
            else:
                message = 'Login failed! Please Try again '

    return render(request, 'account/login.html', context={'form': form, 'message': message})
