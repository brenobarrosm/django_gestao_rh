from django.db import models

from apps.funcionarios.models import Funcionario


class RegistroHoraExtra(models.Model):
    motivo = models.CharField('Motivo', max_length=100)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    horas = models.DecimalField('Horas', max_digits=5, decimal_places=2)

    def __str__(self):
        return self.motivo
