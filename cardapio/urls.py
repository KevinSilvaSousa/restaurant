from django.contrib import admin
from django.urls import path
from cardapio.views import visualizar_cardapio,criar_item_cardapio, deletar_cardapio, listar_cardapio

urlpatterns = [
    path('visualizar_cardapio/', visualizar_cardapio),
    path('criar_item_cardapio/', criar_item_cardapio),
    path('deletar_cardapio', deletar_cardapio),
    path('listar_cardapio/', listar_cardapio), 
]