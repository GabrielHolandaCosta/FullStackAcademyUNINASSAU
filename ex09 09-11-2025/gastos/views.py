from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import CategoriaGasto, Gasto
from .serializers import CategoriaGastoSerializer, GastoSerializer


class CategoriaGastoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciar categorias de gastos.
    Suporta GET, POST, PUT, PATCH, DELETE
    """
    queryset = CategoriaGasto.objects.all()
    serializer_class = CategoriaGastoSerializer
    permission_classes = [IsAuthenticated]


class GastoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciar gastos.
    Suporta GET, POST, PUT, PATCH, DELETE
    """
    serializer_class = GastoSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        # Usuários só veem seus próprios gastos
        return Gasto.objects.filter(usuario=self.request.user)
    
    def perform_create(self, serializer):
        # Define automaticamente o usuário como o usuário logado
        serializer.save(usuario=self.request.user)

