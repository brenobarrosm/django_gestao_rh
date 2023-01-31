from django.contrib import admin

from .models import Documento


@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ['descricao']

    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'
