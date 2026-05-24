from django.db import models


class ClientesModel(models.Model):
    nome = models.CharField(max_length=1000, blank=False)
    cpf = models.CharField(max_length=11, blank=False)
    email = models.EmailField(max_length=1000, blank=False)
    telefone = models.CharField(max_length=20)

    def __str__ (self):
        return self.nome
    