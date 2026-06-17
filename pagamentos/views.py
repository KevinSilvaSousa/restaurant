from django.shortcuts import render
from django.http import HttpResponse
from pedidos.models.pedidosmodels import PedidoModel
from .models import PaymentModel

PAGAMENTO = (
    ('PIX', "PIX"),
    ("CARTAO DE CREDITO", "CARTAO DE CREDITO"),
    ("DEBITO", "DEBITO"),
    ("DINHEIRO", "DINHEIRO"),
)

def criar_pagamento (request, id):
    if request.method == 'POST':
        pedidos = PedidoModel.objects.get(id=id)
        pagamentos = PaymentModel.objects.create(
            forma_pagamento=PAGAMENTO, 
            status='PENDENTE'
        )
        pedidos.pagamento = pagamentos
        pedidos.save()

        return HttpResponse(f'Pagamento criado com sucesso  {pedidos.id}')

