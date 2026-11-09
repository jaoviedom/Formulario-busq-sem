from django.urls import path
from . import views

app_name = "tienda"

urlpatterns = [
    path("buscar/", views.buscar_view, name="buscar"),
    path("productos/<int:pk>/", views.detalle_producto, name="detalle_producto"),
]