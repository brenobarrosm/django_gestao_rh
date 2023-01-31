from django.contrib import admin

from .models import Funcionario


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['nome']

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
