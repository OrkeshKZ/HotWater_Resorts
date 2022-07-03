from django.shortcuts import render
from .models import HotSprings
from django.views.generic import ListView , DetailView

# Create your views here.
class HotWaterListView(ListView):
    model = HotSprings
    template_name = 'home.html'
    

class HotWaterDetailView(DetailView):
    model = HotSprings
    tamplate_name = 'HotWaterPlaces.html'