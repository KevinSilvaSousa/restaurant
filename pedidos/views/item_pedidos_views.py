from django.shortcuts import render
from cardapio.models import CardapioModel
from django.http import HttpResponse
from pedidos.models.itempedidomodels import ItemPedidoModel

def criar_outro_item_pedido(request):
    item_pedido = ItemPedidoModel.objects.create()
    if request.method == 'POST':
        return item_pedido
    

def visualizar_itens_pedido(request, id):
    item_pedido = ItemPedidoModel.objects.filter(id=id)
    if request.method == 'GET':
        return HttpResponse(f"{item_pedido}")
    

def deletar_item(request, id):
    if request.method == 'DELETE':
        item_pedido = ItemPedidoModel.objects.filter(id=id)
        deletar_pedido = ItemPedidoModel.cliente_cardapio
        deletar_pedido.delete()
        print(f"{id} deletado")


    

