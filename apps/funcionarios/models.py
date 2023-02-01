from django.contrib.auth.models import User
from django.db import models

from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa


class Funcionario(models.Model):
    nome = models.CharField('Nome', max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departamentos = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
