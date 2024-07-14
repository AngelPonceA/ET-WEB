from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django import forms

class loginForm(AuthenticationForm):
    username = forms.CharField(max_length=254, label='Usuario')
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')


class registerForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
        
            self.fields['username'].help_text = ''
            self.fields['password1'].help_text = ''
            self.fields['password2'].help_text = ''

            self.fields['username'].label = 'Usuario'
            self.fields['email'].label = 'Correo electronico'
            self.fields['password1'].label = 'Contraseña'
            self.fields['password2'].label = 'Confirmar Contraseña'