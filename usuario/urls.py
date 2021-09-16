from django.contrib import admin
from django.urls import path, include
from .views import *
from . import views

app_name = 'usr'
urlpatterns = [
    path('usr/usr', views.UsuarioC.as_view(), name='usuario')

]
