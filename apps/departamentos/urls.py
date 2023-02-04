from django.urls import path

from .views import (DepartamentoCreate, DepartamentoDelete, DepartamentosList,
                    DepartamentoUpdate)

urlpatterns = [
    path('list/', DepartamentosList.as_view() , name='list_departamentos'),
    path('novo/', DepartamentoCreate.as_view(), name='create_departamento'),
    path('editar/<int:pk>', DepartamentoUpdate.as_view(), name='update_departamento'),
    path('deletar/<int:pk>', DepartamentoDelete.as_view(), name='delete_departamento')
]
