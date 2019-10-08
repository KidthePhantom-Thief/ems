"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from userapp import views

app_name = 'userapp'

urlpatterns = [
    path('login/',views.login,name='login'),
    path('login_logic/',views.login_logic,name='login_logic'),
    path('register/',views.register,name='register'),
    path('register_ok/',views.register_ok,name='register_ok'),
    path('check_all/',views.check_all,name='check_all'),
    path('check_username/',views.check_username,name='check_username'),
    path('create_captcha/',views.create_captcha,name='create_captcha'),
    path('captcha_logic/',views.captcha_logic,name='captcha_logic'),
    path('del_login/',views.del_login,name='del_login'),
]
