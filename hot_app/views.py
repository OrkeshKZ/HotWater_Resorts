from django.shortcuts import render
from .models import HotSprings
from django.views.generic import ListView  # django.views.generic хранилище представлений с библиотеки Джанго

# Create your views here.

class HotSpringsView(ListView):
    model = HotSprings #Указывает из какой модели брать данные!
    template_name = "home.html" #Указывает на какой темплейт выводить данные!
    