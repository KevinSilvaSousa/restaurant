from django.db import models
from clientes.models import ClientesModel
from django.core.validators import MinLengthValidator

class CardapioModel(models.Model):
    TAMANHO = (
        ('PEQUENO', 'BASICA'),
        ('MEDIO', 'INTERMEDIARIO'),
        ('GRANDE', 'ENORME')
    )

    prato = models.CharField(max_length=1000)
    valor = models.DecimalField(
    max_digits=10,
    decimal_places=2
)
    detalhes_prato = models.CharField(max_length=1000000000000)
    tamanho_prato = models.CharField(choices=TAMANHO)

    def __str__ (self):
        return f'{self.prato}: R$ {self.valor} - Detalhes: {self.detalhes_prato} - Tamanho {self.tamanho_prato}'

