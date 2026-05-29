from django.db import models
from clientes.models import ClientesModel
from django.core.validators import MinLengthValidator


class CardapioModel(models.Model):
    prato = models.CharField(max_length=1000)
    valor = models.CharField(max_length=1000000000000)
    detalhes_pedido = models.CharField(validators=[MinLengthValidator(1)])

    def __str__ (self):
        return f'{self.prato}: R$ {self.valor}'

