from django.db import models
from django.contrib.auth.models import User

class Pessoa(models.Model):
    nome = models.CharField(max_length=120)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pessoas')

    def __str__(self):
        return self.nome

class Endereco(models.Model):
    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE, related_name='endereco')
    rua = models.CharField(max_length=200)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=9)

    def __str__(self):
        return f"{self.rua}, {self.numero} - {self.cidade}"
