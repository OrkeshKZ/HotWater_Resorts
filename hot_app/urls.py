from pathlib import Path
from django.urls import path
from .views import HotSpringsView, plaisesDetailView

urlpatterns = [
    path('', HotSpringsView.as_view(), name=('home')),
    # path('plaisesDetail/', TemplateView.as_view(template_name='plaisesDetail.html'), name='plaisesDetail'),
    path('plaisesDetail/<int:pk>', plaisesDetailView.as_view(), name='pleisesDetail')
]

