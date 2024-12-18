from django.shortcuts import render, get_object_or_404
from .models import Tur, Gul

def barcha_gullar(request):
    gullar = Gul.objects.all()
    return render(request, 'index.html', {'gullar': gullar})

def gullar_turlar_boyicha(request, tur_id):
    turlar = get_object_or_404(Tur, id=tur_id)
    gullar = turlar.gullar.all()
    return render(request, 'index.html', {'turlar': turlar, 'gullar': gullar})

def bitta_gul(request, gul_id):
    gul = get_object_or_404(Gul, id=gul_id)
    return render(request, 'index.html', {'gul': gul})
