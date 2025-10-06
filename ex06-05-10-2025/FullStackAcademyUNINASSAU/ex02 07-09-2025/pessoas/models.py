from django.db import models

class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=120)
    cpf = models.CharField('CPF', max_length=14, unique=True)
    email = models.EmailField('E-mail', blank=True, null=True)
    telefone = models.CharField('Telefone', max_length=20, blank=True)
    data_nascimento = models.DateField('Data de nascimento', blank=True, null=True)
    rg = models.CharField('RG', max_length=20, blank=True)
    endereco = models.CharField('Endereço', max_length=255, blank=True)
    bairro = models.CharField('Bairro', max_length=100, blank=True)

    def __str__(self):
        return f"{self.nome} ({self.cpf})"
