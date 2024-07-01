from django import forms

class RegisterForm(forms.Form):
    correo = forms.CharField()
    nombre = forms.CharField()
    contraseña = forms.CharField(widget=forms.PasswordInput)

class LoginForm(forms.Form):
    correo = forms.CharField()
    contraseña = forms.CharField(widget=forms.PasswordInput)
