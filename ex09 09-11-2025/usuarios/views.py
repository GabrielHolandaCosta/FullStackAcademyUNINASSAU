from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import PerfilUsuario
from .serializers import UserSerializer, PerfilUsuarioSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciar usuários.
    Suporta GET, POST, PUT, PATCH, DELETE
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class PerfilUsuarioViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciar perfis de usuários.
    Suporta GET, POST, PUT, PATCH, DELETE
    """
    queryset = PerfilUsuario.objects.all()
    serializer_class = PerfilUsuarioSerializer
    permission_classes = [IsAuthenticated]

