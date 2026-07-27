from django.shortcuts import render

from django.shortcuts import render
from .models import Producto

def productos(request):
    texto = {
        "productos": Producto.objects.all()
    }

    return render(request, "productos.html", texto)