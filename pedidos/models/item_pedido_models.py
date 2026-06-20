from django.db import models
from clientes.models import ClientesModel
from cardapio.models import CardapioModel
from .pedidosmodels import PedidoModel
from pagamentos.models import PaymentModel

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
        pagamento = models.OneToOneField(PaymentModel, on_delete=models.CASCADE, null=True, blank=True)

        def subtotal(self): 
            return self.prato.preco * self.quantidade

        def __str__(self):
            return f"{self.pedido}" 