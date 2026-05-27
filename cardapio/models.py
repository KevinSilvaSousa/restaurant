from django.db import models
from clientes.models import ClientesModel
from django.core.validators import MinLengthValidator


class CardapioModel(models.Model):

    cliente_cardapio = models.ForeignKey(ClientesModel, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    prato = models.CharField(max_length=1000)
    detalhes_pedido = models.CharField(validators=[MinLengthValidator(1)])
    status_pedido = models.CharField(max_length=30)

    def __str__ (self):
        return self.prato

