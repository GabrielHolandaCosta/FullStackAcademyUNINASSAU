from django.urls import path
from .views import perfil, gerencia, usuario_comum

urlpatterns = [
    path('perfil/', perfil, name='perfil'),
    path('gerencia/', gerencia, name='gerencia'),
    path('usuario-comum/', usuario_comum, name='usuario_comum'),
]
