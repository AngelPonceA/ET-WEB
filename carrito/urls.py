from django.urls import path
from . import views

urlpatterns = [
    path('carrito/', views.carrito, name = 'carrito'),
    # path('agregar/<int:id_auto>/', views.agregar_auto, name="agregar_auto"),
    # path('eliminar/<int:id_auto>/', views.eliminar_auto, name="eliminar_auto"),
    # path('restar/<int:id_auto>/', views.restar_auto, name="restar_auto"),
    # path('limpiar/', views.limpiar_carrito, name="limpiar_carrito"),
]