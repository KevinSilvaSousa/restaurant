from django.shortcuts import render
from cardapio.models import CardapioModel
from django.http import HttpResponse
from .pedidosmodels import PedidoModel



def criar_pedido(request):
    pedido = PedidoModel.objects.create()
    if request.method == 'POST':
        return pedido    
    return HttpResponse('Pedido criado ou existente!')


def visualizar_seu_pedido(request, id):
    pedido = PedidoModel.objects.filter(id=id)
    if request.method == 'GET':
        
        return HttpResponse(pedido)
    return HttpResponse(f'Pedido do id: {id}')


def deletar_pedido(request, id):
    if request.method == 'DELETE':
        pedido = PedidoModel.objects.filter(id=id)
        deletar_pedido = PedidoModel.cliente_cardapio
        deletar_pedido.delete()
        print(f"{id} deletado")
    
    return HttpResponse('Pedido deletado!')


def atualizar_pedido(request, id, cliente_cardapio):
    if request.method == 'PUT':
        pedido = PedidoModel.objects.filter(id=id)
        atualizar_pedido = pedido.get()
        pedido.cliente_cardapio = cliente_cardapio
        atualizar_pedido.save()
        return HttpResponse("Pedido Atualizado")
    

def listar_pedidos(request, id):
    if request.method == 'GET':
        pedidos = PedidoModel.objects.filter(id=id)
        text = " "
        for p in pedidos:
            text += p.nome + "<br></br>"
