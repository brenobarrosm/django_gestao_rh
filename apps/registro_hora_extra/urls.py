from django.urls import path

from .views import HoraExtraEdit, HoraExtraList

urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_hora_extra'),
    path('editar/<int:pk>', HoraExtraEdit.as_view(), name='edit_hora_extra'),
]
