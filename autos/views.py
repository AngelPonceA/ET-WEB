from django.shortcuts import get_object_or_404, render
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

# def ficha(request):
#     autos = auto.objects.all() 
#     context = {
#         'autos': autos,
#     }
#     return render(request,'autos/ficha.html', context)

def ficha(request, id_auto):
    auto = get_object_or_404(auto, id=id_auto)
    return render(request, 'autos/ficha.html', {'auto': auto})
