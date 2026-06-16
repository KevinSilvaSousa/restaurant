from django.db import models
from clientes.models import ClientesModel
from cardapio.models import CardapioModel
from .pedidosmodels import PedidoModel

class ItemPedido(models.Model):
        pedido = models.ForeignKey(
        ClientesModel,
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