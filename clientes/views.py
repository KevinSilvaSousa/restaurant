from django.shortcuts import render
from .models import ClientesModel
from django.http import HttpResponse

# Create your views here.


def criar_cliente(request):
    nome_cliente = ClientesModel.objects.create()
    return HttpResponse ('cliente criado!')