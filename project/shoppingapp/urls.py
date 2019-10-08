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

from shoppingapp import views

app_name = 'shoppingapp'

urlpatterns = [
    path('car/', views.car, name='car'),
    path('add_cart/', views.add_cart, name='add_cart'),
    path('del_car_cart/', views.del_car_cart, name='del_car_cart'),
    path('change_car_cart/', views.change_car_cart, name='change_car_cart'),
    path('del_cart/', views.del_cart, name='del_cart'),

]
