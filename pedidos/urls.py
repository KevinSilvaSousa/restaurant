from django.urls import path
from pedidos.views.pedidos_views import criar_pedido, visualizar_seu_pedido,  atualizar_pedido,deletar_pedido
from pedidos.views.item_pedidos_views import criar_outro_item_pedido, visualizar_itens_pedido, deletar_item

urlpatterns = [
    path('criar_pedido/', criar_pedido),
    path('visualizar_pedido/<int:id>', visualizar_seu_pedido),
    path('atualizar_pedido/<int:id>', atualizar_pedido),
    path('deletar_pedido/', deletar_pedido),

    path('criar_outro_item_pedido/', criar_outro_item_pedido),
    path('visualizar_itens_pedido/<int:id>', visualizar_itens_pedido),
    path('deletar_item/<int:id>', deletar_item),
]