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
from rest_framework.response import Response
from .serializer import LogMessageSerializer
from rest_framework.decorators import api_view
from rest_framework import status
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

# include rest framework and make the api for the log messages 
# get all the messages
@api_view(['GET','POST'])
def all_messages(request):
    if request.method=='GET':
        log=LogMessage.objects.all()
        serializer=LogMessageSerializer(log,many=True)
        return Response({
        "Status":True,
        "data":serializer.data,
        "message":"Success"})
    
    if request.method=='POST':
        data=request.data
        data['log_date']=datetime.datetime.now()
        serializer=LogMessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        return Response({
        "Status":True,
        "data":serializer.data,
        "messages":"Message Created Succesfully "},
        status=status.HTTP_201_CREATED)
    

