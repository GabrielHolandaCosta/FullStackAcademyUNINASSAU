from rest_framework import serializers
from .models import CategoriaGasto, Gasto
from django.contrib.auth.models import User


class CategoriaGastoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaGasto
        fields = ['id', 'nome', 'descricao']
        read_only_fields = ['id']


class GastoSerializer(serializers.ModelSerializer):
    categoria_nome = serializers.CharField(source='categoria.nome', read_only=True)
    usuario_username = serializers.CharField(source='usuario.username', read_only=True)
    
    class Meta:
        model = Gasto
        fields = ['id', 'usuario', 'usuario_username', 'categoria', 'categoria_nome', 
                  'descricao', 'valor', 'data', 'observacoes', 'criado_em', 'atualizado_em']
        read_only_fields = ['id', 'criado_em', 'atualizado_em']

