from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegisterForm, LoginForm
from .models import Cliente

def clienteAdd(request): 
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            cliente = Cliente(
                Correo=form.cleaned_data['correo'],
                Nombre=form.cleaned_data['nombre'],
                Clave=form.cleaned_data['contraseña']
            )
            cliente.save()
            
            context = {
                "mensaje": f"Usuario {form.cleaned_data['nombre']} creado",
                'form': RegisterForm()
            }
            return render(request, 'clientes/register.html', context)
    else:
        form = RegisterForm()

    context = {
        'form': form,
    }
    return render(request, 'clientes/register.html', context)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirige a la página principal después de iniciar sesión
            else:
                form.add_error(None, 'Correo electrónico o contraseña incorrectos')
    else:
        form = LoginForm()
    return render(request, 'clientes/login.html', {'form': form})