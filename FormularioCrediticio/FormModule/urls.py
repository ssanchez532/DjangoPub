from django.urls import path
from django.contrib import admin
from .views import home, datos
urlpatterns = [
    path('', home, name="home"),
    path('home.html', home, name="home"),
    path('datos.html', datos, name="datos"),
]