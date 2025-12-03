from django.db import models
from django.contrib.auth.models import User


class CategoriaGasto(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True)
    
    def __str__(self):
        return self.nome


class Gasto(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='gastos')
    categoria = models.ForeignKey(CategoriaGasto, on_delete=models.SET_NULL, null=True, related_name='gastos')
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    observacoes = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-data', '-criado_em']
    
    def __str__(self):
        return f"{self.descricao} - R$ {self.valor}"

