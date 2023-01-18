from django.urls import path
from hello import views
from hello.models import LogMessage

urlpatterns = [
   path("", views.home, name="home1"),
   path("about/", views.about, name="about"),
   path("contact/", views.contact, name="contact"),
   path("log/", views.log_message, name="log"),
]