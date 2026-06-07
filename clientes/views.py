from django.shortcuts import render
from .models import ClientesModel
from django.http import HttpResponse
from django.shortcuts import get_object_or_404


def buscar_id_cliente(request, id):
    cliente = ClientesModel.objects.get(id=id)
    if request.method == 'GET':
         return HttpResponse(cliente.nome) 
    
    if cliente == 500:
        cliente =  get_object_or_404(ClientesModel, id=id)

    
    
def criar_cliente(request):
    nome_cliente = ClientesModel.objects.create()
    if request.method == "POST":
        return nome_cliente
    return HttpResponse ('cliente criado!')


def atualizar_cliente(request, id, nome):
    if request.method == 'PUT':
        nome_cliente = ClientesModel.objects.filter(id=id)
        cliente_atualizar = nome_cliente.get()
        cliente_atualizar.nome = nome
        cliente_atualizar.save()
        return HttpResponse ('Cliente atualizado!')
    


def deletar_cliente(request, id, nome):
    if request.method == 'DELETE':
        nome_cliente = ClientesModel.objects.filter(id=id)
        deletar = nome_cliente.get()
        deletar.delete()
        print(f"cliente {nome} Deletado!")
    return HttpResponse ('Cliente Deletado!')