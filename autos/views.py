from django.shortcuts import render
from .models import auto

# Create your views here.

def home(request):
    autos = auto.objects.all() 
    context = {
        'autos': autos,
    }
    return render(request,'autos/home.html',context)

