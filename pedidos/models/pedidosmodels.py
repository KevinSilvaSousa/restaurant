from django.db import models
from clientes.models import ClientesModel
from cardapio.models import CardapioModel
from pagamentos.models import PaymentModel

class PedidoModel(models.Model):
    """Esse model será usado para representar um prato/produto do restaurante."""
    STATUS_PEDIDO = (
    ('PENDENTE', 'Pendente'),
    ('EM_PREPARO', 'Em preparo'),
    ('PRONTO', 'Pronto'),
    ('SAIU_PARA_ENTREGA', 'Saiu para entrega'),
    ('ENTREGUE', 'Entregue'),
    ('CANCELADO', 'Cancelado'),
)

    
    pedido_cliente = models.ForeignKey(ClientesModel, on_delete=models.CASCADE, related_name='pedidos')
    prato_cliente = models.ForeignKey(CardapioModel, on_delete=models.CASCADE, related_name='pedidos')    
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    status_pedido = models.CharField(max_length=20, choices=STATUS_PEDIDO)
    quantidade_kg = models.IntegerField(default=0)
    quantidade_pedido = models.IntegerField(default=1)
    pagamento = models.OneToOneField(PaymentModel, on_delete=models.CASCADE, related_name='pagamento', null=True, blank=True)

    def __str__(self):
        return f'{self.pedido_cliente}: {self.prato_cliente}'
    

    """
    pedido = Aqui seleciona o cliente que quer fazer o pedido
    prato = Aqui seleciona o prato que existe no CardapioModel
    """