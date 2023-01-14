from django.shortcuts import render
from django.utils.timezone import datetime
from django.http import HttpResponse
from .models import LogMessage
from hello.forms import LogMessageForm
from django.shortcuts import redirect
from django.views.generic import ListView
import datetime


class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage
    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

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
            return redirect("home")  # here we use the redirect mehtod for not use the hard coded 
            # here we use this also 
            #return render(request,"hello/home.html")
    else:
        return render(request, "hello/log_message.html", {"form": form})