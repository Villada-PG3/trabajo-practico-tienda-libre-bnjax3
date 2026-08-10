from django.shortcuts import render

from django.shortcuts import render
from .models import *

def productos(request):
    texto = {
        "productos": Producto.objects.all(),
        "categorias": Categoria.objects.all()
    }
    return render(request, "productos.html", texto)


def home(request):
    texto = {
        "productos": Producto.objects.all(),
        "categorias": Categoria.objects.all()
    }
    return render(request, "home.html", texto)

def acerca(request):
    return render(request, "acerca.html")