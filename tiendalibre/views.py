from django.shortcuts import render

from django.shortcuts import render
from .models import *

def productos(request):
    texto = {
        "productos": Producto.objects.all(),
        "categorias": Categoria.objects.all()
    }
    print(texto)
    return render(request, "productos.html", texto)