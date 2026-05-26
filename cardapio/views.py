from django.shortcuts import render
from cardapio.models import CardapioModel
from django.http import HttpResponse

def criar_pedido(request, id):
    pedido = CardapioModel.objects.create(id=id)
    if request.method == 'POST':
        return pedido    
    return HttpResponse('Pedido criado ou existente!')


def visualizar_pedido(request, id):
    pedido = CardapioModel.objects.get(id)
    if request.method == 'GET':
        return pedido
    return HttpResponse(f'Pedido do id: {id}')


def deletar_pedido(request, id):
    if request.method == 'DELETE':
        pedido = CardapioModel.objects.get(id)
        

    