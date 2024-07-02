from django.shortcuts import render
from .models import auto

# Create your views here.

def home(request):
    autos = auto.objects.all() 
    context = {
        'autos': autos,
    }
    return render(request,'autos/home.html', context)

def filtrar(request):
    query = request.GET.get('query', '')
    if query:
        autos = auto.objects.filter(modelo__icontains=query)
    else:
        autos = auto.objects.all()
    return render(request, 'autos/home.html', {'autos': autos, 'query': query})