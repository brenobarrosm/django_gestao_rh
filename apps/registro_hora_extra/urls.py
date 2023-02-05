from django.urls import path

from .views import (HoraExtraCreate, HoraExtraDelete, HoraExtraEdit,
                    HoraExtraList)

urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_hora_extra'),
    path('editar/<int:pk>', HoraExtraEdit.as_view(), name='edit_hora_extra'),
    path('delatar/<int:pk>', HoraExtraDelete.as_view(), name='delete_hora_extra'),
    path('novo/', HoraExtraCreate.as_view(), name='create_hora_extra')
]
