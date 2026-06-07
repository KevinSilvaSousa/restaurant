from django.urls import path
from pedidos.pedidos_views import criar_pedido, visualizar_seu_pedido, atualizar_pedido,deletar_pedido

urlpatterns = [
    path('criar_pedido/', criar_pedido),
    path('visualizar_pedido/<int:id>', visualizar_seu_pedido),
    path('atualizar_pedido/<int:id>', atualizar_pedido),
    path('deletar_pedido/', deletar_pedido),
]