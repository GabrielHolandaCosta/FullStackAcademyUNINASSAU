from django.db import models

class Estado(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=2)
    def __str__(self): return f"{self.nome} ({self.sigla})"

class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, related_name='cidades')
    def __str__(self): return f"{self.nome} - {self.estado.sigla}"

class Logradouro(models.Model):
    nome = models.CharField(max_length=200)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, related_name='logradouros')
    def __str__(self): return f"{self.nome}, {self.cidade.nome}"

class CEP(models.Model):
    codigo = models.CharField(max_length=20)
    logradouro = models.ForeignKey(Logradouro, on_delete=models.CASCADE, related_name='ceps')
    def __str__(self): return self.codigo

class Empresa(models.Model):
    nome = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=18, blank=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True)
    def __str__(self): return self.nome

class Funcionario(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=14, blank=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='funcionarios')
    cargo = models.CharField(max_length=100, blank=True)
    data_admissao = models.DateField(null=True, blank=True)
    def __str__(self): return self.nome
