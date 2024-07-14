from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from . import models, forms
from .models import Cliente

def register_view(request):
    if(request.user.is_authenticated):
        return redirect('home')
    if request.method == 'POST':
        form = forms.registerForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'register/register.html', {'form': form, 'error': 'Datos invalidos'}) #Sin uso
    return render(request, 'register/register.html', {'form': forms.registerForm})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'login/login.html', {'form': form, 'error': 'Nombre de usuario o contraseña incorrectos'}) #Sin uso
        else:
            return render(request, 'login/login.html', {'form': form, 'error': 'Datos inválidos'}) #Sin uso
    else:
        form = AuthenticationForm()
        return render(request, 'login/login.html', {'form': form})

# def login_view(request):
#     if request.method == 'POST':
#         form = forms.loginForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=email, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')  # Redirige a la página principal después de iniciar sesión
#             else:
#                 form.add_error(None, 'Correo electrónico o contraseña incorrectos')
#     else:
#         form = forms.loginForm()
#     return render(request, 'login/login.html', {'form': forms.loginForm})


def close_sesion(request):
    logout(request)
    return redirect('home')


def aboutUs(request):
    return render(request, 'aboutUs/aboutUs.html')
