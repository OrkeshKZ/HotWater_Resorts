from django.urls import path
from .views import HotWaterListView, HotWaterDetailView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', HotWaterListView.as_view(), name='home'),
    path('HotWater/<int:pk>/', HotWaterDetailView.as_view(), name='HotWaterPlaces'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
