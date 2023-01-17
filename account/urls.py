from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from account import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.SignUp, name='signup'),
    path('login/',views.login_page,name='loginn'),
]