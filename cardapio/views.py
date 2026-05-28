from django.shortcuts import render
from cardapio.models import CardapioModel
from django.http import HttpResponse


def visualizar_cardapio(request):
    pedido = CardapioModel.objects.all()
    if request.method == 'GET':
        return HttpResponse(pedido)