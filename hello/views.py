from django.shortcuts import render
from django.utils.timezone import datetime
from django.http import HttpResponse
from .models import LogMessage
from hello.forms import LogMessageForm
from django.shortcuts import redirect
from django.views.generic import ListView
import datetime
from django.http import JsonResponse
import json
from .models import LogMessage

def home(request):
    lg=LogMessage.objects.values()
    return JsonResponse(list(lg),safe=False)


def about(request):
    return render(request, "hello/about.html")

def contact(request):
    return render(request, "hello/contact.html")


# make the view for the data 
def  log_message(request):
    form = LogMessageForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.datetime.now()
            message.save()
            return redirect("home1")
    else:
        return render(request, "hello/log_message.html", {"form": form})

        