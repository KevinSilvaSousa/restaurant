from django.db import models
from clientes.models import ClientesModel
from cardapio.models import CardapioModel

class ItemPedidoModel(models.Model):
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
    prato_cliente = models.ManyToManyField(CardapioModel, through='ItemPedidoModel', related_name='pedidos', choices=STATUS_PEDIDO)
    tamanho_lanche = models.CharField(choices=TAMANHO)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now_add=True)

