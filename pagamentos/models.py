from django.db import models
from pedidos.models.pedidosmodels import PedidoModel

# Create your models here.

class PaymentModel(models.Model):
    PAGAMENTO = (
    ('PIX', "PIX"),
    ("CARTAO DE CREDITO", "CARTAO DE CREDITO"),
    ("DEBITO", "DEBITO"),
    ("DINHEIRO", "DINHEIRO"),
)
    STATUS = (
        ('PENDENTE', 'Pendente'),
        ('APROVADO', 'Aprovado'),
        ('RECUSADO', 'Recusado'),
    )
    pedido = models.OneToOneField(
        PedidoModel,
        on_delete=models.CASCADE,
        related_name='pagamento'
    )

    forma_pagamento = models.CharField(
        max_length=20,
        choices=PAGAMENTO
    )

    valor = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default='PENDENTE'
    )

    data_pagamento = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Pagamento Pedido #{self.pedido.id}"