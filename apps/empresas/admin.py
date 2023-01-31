from django.contrib import admin

from .models import Empresa


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ['nome']

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
