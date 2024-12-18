from django.contrib import admin
from .models import Tur, Gul

@admin.register(Tur)
class TurAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom')

@admin.register(Gul)
class GulAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'tur')
