from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gullar/', views.barcha_gullar, name='barcha_gullar'),
    path('turlar/<int:tur_id>/', views.gullar_turlar_boyicha, name='gullar_turlar_boyicha'),
    path('gul/<int:gul_id>/', views.bitta_gul, name='bitta_gul'),
]
