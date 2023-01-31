from django.db import models


class Departamento(models.Model):
    nome = models.CharField('Nome', max_length=70)

    def __str__(self):
        return self.nome
