from django.db import models

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
        'pedidos.PedidoModel',
        related_name='pedidos',
        on_delete=models.CASCADE
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

    def save(self, *args, **kwargs):
        self.valor = self.pedido.valor_total()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Pagamento Pedido #{self.pedido.pedido_cliente}"