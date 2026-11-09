# Importamos utilidades para renderizar plantillas y para devolver un 404 si no existe el objeto
from django.shortcuts import render, get_object_or_404
from .models import Producto
from django.views.decorators.http import require_GET
from core.ia.buscador import buscar_productos


# Vista de detalle de un producto
def detalle_producto(request, pk):
    # Busca un producto por clave primaria (pk); si no existe, devuelve 404 automáticamente
    producto = get_object_or_404(Producto, pk=pk)
    # Pasamos el objeto producto a la plantilla
    return render(request, "detalle_producto.html", {"producto": producto})

@require_GET # Es un decorador de Django que restringe la vista para solo aceptar solicitudes GET.
def buscar_view(request):
  q = request.GET.get("q", "")
  resultados = buscar_productos(q, k=5) if q else []
  return render(request, "buscar.html", {"q": q, "resultados": resultados})
