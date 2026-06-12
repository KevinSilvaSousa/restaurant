from django.shortcuts import render
from cardapio.models import CardapioModel
from django.http import HttpResponse
from django.shortcuts import get_object_or_404


def visualizar_cardapio(request):
    pedido = CardapioModel.objects.all()
    if request.method == 'GET':
        return HttpResponse(pedido)
    

def criar_item_cardapio(request, id):
    criar_item_cliente = CardapioModel.objects.create(id=id)
    if request.method == 'POST':
        return criar_item_cliente
    return HttpResponse("Novo item do cardapio criado!")


def deletar_cardapio(request, id):
    if request.method == 'DELETE':
        pedido = get_object_or_404(CardapioModel, id=id)
        pedido_get = pedido.get()
        pedido_get.delete()
        return HttpResponse("Pedido Deletado")
    

def listar_cardapio(request):
    if request.method == 'GET':
        cardapios = CardapioModel.objects.all()
        texto = " "
        for cardapio in cardapios:
            texto+= cardapios.nome + " <br></br>"