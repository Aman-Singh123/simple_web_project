from django.urls import path
from hello import views
from hello.models import LogMessage

urlpatterns = [
   path("", views.home, name="home1"),
   path("about/", views.about, name="about"),
   path("contact/", views.contact, name="contact"),
   path("log/", views.log_message, name="log"),
   # make the the or url for the get all the message using postman or api 
   path("list/",views.all_messages,name="all_message"),
   # create url for the to send the message 
   path("create/",views.all_messages , name="create_message"),
]