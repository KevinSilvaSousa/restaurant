from django.db import models
from clientes.models import ClientesModel
from .pedidosmodels import PedidoModel
from cardapio.models import CardapioModel

class ItemPedido(models.Model):
        pedido = models.ForeignKey(
        PedidoModel,
        on_delete=models.CASCADE,
        related_name='itens'
        )
        prato = models.ForeignKey(
        CardapioModel,
        on_delete=models.CASCADE
        )
        quantidade = models.IntegerField()

        def __str__(self):
            return f"{self.pedido}" 