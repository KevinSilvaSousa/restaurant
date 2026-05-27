from django.db import models
from clientes.models import ClientesModel
from django.core.validators import MinLengthValidator


class CardapioModel(models.Model):
    STATUS_PEDIDO = (
    ('PENDENTE', 'Pendente'),
    ('EM_PREPARO', 'Em preparo'),
    ('PRONTO', 'Pronto'),
    ('SAIU_PARA_ENTREGA', 'Saiu para entrega'),
    ('ENTREGUE', 'Entregue'),
    ('CANCELADO', 'Cancelado'),
)

    cliente_cardapio = models.ForeignKey(ClientesModel, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    prato = models.CharField(max_length=1000)
    detalhes_pedido = models.CharField(validators=[MinLengthValidator(1)])
    status_pedido = models.CharField(max_length=30, choices=STATUS_PEDIDO)

    def __str__ (self):
        return self.prato

