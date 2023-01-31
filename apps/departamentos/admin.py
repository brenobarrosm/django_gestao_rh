from django.contrib import admin

from .models import Departamento


@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ['nome']

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
