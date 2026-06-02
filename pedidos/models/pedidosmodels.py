from django.db import models
from clientes.models import ClientesModel
from cardapio.models import CardapioModel
#from .itempedidomodels import ItemPedidoModel
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
    
    TAMANHO = (
        ('PEQUENO', 'BASICA'),
        ('MEDIO', 'INTERMEDIARIO'),
        ('GRANDE', 'ENORME')
    )

    pedido_cliente = models.ForeignKey(ClientesModel, on_delete=models.CASCADE)
    prato_cliente = models.ForeignKey(CardapioModel,on_delete=models.CASCADE)
    #prato_cardapio = models.ForeignKey(ItemPedidoModel,on_delete=models.CASCADE)
    tamanho_lanche = models.CharField(max_length=20,choices=TAMANHO)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    status_pedido = models.CharField(max_length=20, choices=STATUS_PEDIDO)


    def __str__(self):
        return f'{self.pedido_cliente}: {self.prato_cliente}'