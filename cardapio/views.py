from django.shortcuts import render
from cardapio.models import CardapioModel
from django.http import HttpResponse


def visualizar_cardapio(request):
    pedido = CardapioModel.objects.all()
    if request.method == 'GET':
        return HttpResponse(pedido)
    

def criar_item_cardapio(request, id):
    criar_item_cliente = CardapioModel.objects.create(id=id)
    if request.method == 'POST':
        return criar_item_cliente
    return HttpResponse("Novo item do cardapio criado!")