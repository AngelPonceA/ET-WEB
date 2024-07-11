from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.clienteAdd, name='register'),
    path('login/', views.login_view, name='login'),
    path('aboutUs/', views.aboutUs, name='aboutUs'),
]
