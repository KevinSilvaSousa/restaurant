from django.contrib import admin
from django.urls import path, include
from clientes.views import criar_cliente, buscar_id_cliente, atualizar_cliente, deletar_cliente

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('clientes.urls')),
    path('clientes/', include('cardapio.urls')),
]
