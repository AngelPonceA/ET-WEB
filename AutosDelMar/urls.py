from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('autos/', include('autos.urls')),
    path('clientes/', include('clientes.urls')),
    path('home', RedirectView.as_view(url='/autos/', permanent=True)),    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
