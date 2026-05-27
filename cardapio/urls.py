from django.contrib import admin
from django.urls import path
from cardapio.views import criar_pedido, visualizar_pedido, deletar_pedido, atualizar_pedido

urlpatterns = [
    path('criar_pedido/', criar_pedido),
    path('visualizar_pedido/<int:id>', visualizar_pedido),
    path('deletar_pedido/<int:id>', deletar_pedido),
    path('atualizar_pedido/<int:id>', atualizar_pedido),
]