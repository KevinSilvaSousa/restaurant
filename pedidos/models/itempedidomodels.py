from django.db import models
from clientes.models import ClientesModel
from cardapio.models import CardapioModel
from pedidos.models.pedidosmodels import PedidoModel

class ItemPedidoModel(models.Model):
    pedido = models.ForeignKey(PedidoModel,on_delete=models.CASCADE)
    prato = models.ForeignKey(CardapioModel,on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)

