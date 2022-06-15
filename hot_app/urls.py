from django.urls import path
from .views import HotSpringsView

urlpatterns = [
    path('', HotSpringsView.as_view(), name=('home')),
]
