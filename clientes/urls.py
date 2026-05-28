from django.urls import path
from clientes.views import criar_cliente, buscar_id_cliente, atualizar_cliente, deletar_cliente

urlpatterns = [
    path('buscar_cliente/<int:id>', buscar_id_cliente),
    path('criar_cliente/', criar_cliente),
    path('atualizar_cliente/<int:id>', atualizar_cliente),
    path('deletar_cliente/', deletar_cliente),
]