from django.db import models
from clientes.models import ClientesModel
from cardapio.models import CardapioModel
from pagamentos.models import PaymentModel
from decimal import Decimal

class PedidoModel(models.Model):
    STATUS_PEDIDO = (
    ('AGUARDANDO_PAGAMENTO', 'Aguardando Pagamento'),
    ('PAGO', 'Pago'),
    ('PENDENTE', 'Pendente'),
    ('EM_PREPARO', 'Em Preparo'),
    ('PRONTO', 'Pronto'),
    ('SAIU_PARA_ENTREGA', 'Saiu para Entrega'),
    ('ENTREGUE', 'Entregue'),
    ('CANCELADO', 'Cancelado'),
)
    
    pedido_cliente = models.ForeignKey(
        ClientesModel,
        on_delete=models.CASCADE,
        related_name='pedidos'
    )

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    status_pedido = models.CharField(
        max_length=20,
        choices=STATUS_PEDIDO
    )

    def valor_total(self):
        total = Decimal("0.00")

        for item in self.itens.all():
            total += item.prato.valor * item.quantidade

        return total
    
    def __str__ (self):
        return f"{self.id} - {self.pedido_cliente}"