from rest_framework import serializers
from django.contrib.auth.models import User
from .models import PerfilUsuario


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'date_joined']
        read_only_fields = ['id', 'date_joined']


class PerfilUsuarioSerializer(serializers.ModelSerializer):
    usuario = UserSerializer(read_only=True)
    
    class Meta:
        model = PerfilUsuario
        fields = ['id', 'usuario', 'telefone', 'data_nascimento', 'endereco']
        read_only_fields = ['id']

