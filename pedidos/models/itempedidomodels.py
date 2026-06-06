from django.db import models
from clientes.models import ClientesModel
from cardapio.models import CardapioModel
from pedidos.models.pedidosmodels import PedidoModel

class ItemPedidoModel(models.Model):
    """Esse model será usando para representar os itens dentro de um pedido do cliente. """
    pedido = models.ForeignKey(PedidoModel,on_delete=models.CASCADE)
    prato = models.ForeignKey(CardapioModel, on_delete=models.CASCADE)
    quantidade_kg = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.cliente}'

