from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class loginForm(AuthenticationForm):
    username = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'placeholder': 'Usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))

class registerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        labels = {
            'username': 'Nombre',
            'email': 'Correo electrónico',
            'password': 'Contraseña',
        }

# class loginForm(forms.Form):
#     correo = forms.CharField()
#     contraseña = forms.CharField(widget=forms.PasswordInput)
