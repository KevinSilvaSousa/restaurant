from django.shortcuts import render
from .models import ClientesModel
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from pedidos.models.item_pedido_models import ItemPedido


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


def listar_clientes(request):
    if request.method == 'GET':
        clientes = ClientesModel.objects.all()
        texto = " "

        for cliente in clientes:
            texto+= cliente.nome + " <br></br>"

    return HttpResponse(texto)


def mostrar_pedido_cliente(request, id):
    if request.method == 'GET':
        cliente_pedido_todos = ClientesModel.objects.filter(id=id)
        itens = ItemPedido.objects.filter(id=id)
        text = " \n"

        for cliente in cliente_pedido_todos:
            text += f"Cliente: {cliente.nome} \n\n"
        for pedido in  itens:
            text += f"Pedido: {pedido.pedido} \n\n"
        
        return HttpResponse(f"{text}")
            

 