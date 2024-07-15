from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from autos.models import auto
from . import carrito

@login_required(login_url='login/login')
def carrito(request):
    return render(request,'carrito/carrito.html')

# def agregar(request, auto.id_auto):
#     carrito = Carrito(request)
#     producto = auto.objects.get(id = id_auto)
#     carrito.agregar(auto)
#     return redirect("carrito: carrito")

# def eliminar(request, auto.id_auto):
#     carrito = Carrito(request)
#     producto = auto.objects.get(id = id_auto)
#     carrito.eliminar(auto)
#     return redirect("carrito: carrito")

# def restar(request, auto.id_auto):
#     carrito = Carrito(request)
#     producto = auto.objects.get(id = id_auto)
#     carrito.restar(auto)
#     return redirect("carrito: carrito")

# def limpiar(request):
#     carrito = Carrito(request)
#     carrito.limpiar(auto)
#     return redirect("carrito: carrito")