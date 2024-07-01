from django.shortcuts import render, redirect
from .forms import ClienteForm
from .models import Cliente

def login(request):
    context = {}
    return render (request, 'clientes/login.html', context)



def clienteAdd(request): 
    if request.method =='POST':
        correo = request.POST['Correo']
        nombre = request.POST['Nombre']
        clave = request.POST['Clave']
        
        obj = Cliente.objects.create( Correo = correo,
                                     Nombre = nombre,
                                     Clave =clave)
        obj.save()
        
        context = {
            "mensaje" : f"usuario {nombre} creado",
            'form' : ClienteForm()
        }
        return render(request, 'clientes/register.html', context)
    else:
        form = ClienteForm()  # Crear una instancia del formulario vacía

    context = {
        'form': form,
    }
    return render(request, 'clientes/register.html', context)



