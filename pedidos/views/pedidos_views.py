from django.shortcuts import render
from cardapio.models import CardapioModel
from django.http import HttpResponse



def criar_pedido(request):
    pedido = CardapioModel.objects.create()
    if request.method == 'POST':
        return pedido    
    return HttpResponse('Pedido criado ou existente!')


def visualizar_seu_pedido(request, id):
    pedido = CardapioModel.objects.filter(id=id)
    if request.method == 'GET':
        
        return HttpResponse(pedido)
    return HttpResponse(f'Pedido do id: {id}')


def deletar_pedido(request, id):
    if request.method == 'DELETE':
        pedido = CardapioModel.objects.filter(id=id)
        deletar_pedido = CardapioModel.cliente_cardapio
        deletar_pedido.delete()
        print(f"{id} deletado")
    
    return HttpResponse('Pedido deletado!')


def atualizar_pedido(request, id, cliente_cardapio):
    if request.method == 'PUT':
        pedido = CardapioModel.objects.filter(id=id)
        atualizar_pedido = pedido.get()
        pedido.cliente_cardapio = cliente_cardapio
        atualizar_pedido.save()
        return HttpResponse("Pedido Atualizado")