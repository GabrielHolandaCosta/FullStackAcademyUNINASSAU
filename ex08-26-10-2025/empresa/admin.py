from django.contrib import admin
from .models import Estado, Cidade, Logradouro, CEP, Empresa, Funcionario

@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('nome','sigla')
    search_fields = ('nome','sigla')

@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ('nome','estado')
    list_select_related = ('estado',)
    search_fields = ('nome',)
    list_filter = ('estado',)

@admin.register(Logradouro)
class LogradouroAdmin(admin.ModelAdmin):
    list_display = ('nome','cidade')
    list_select_related = ('cidade','cidade__estado')
    search_fields = ('nome','cidade__nome')

@admin.register(CEP)
class CEPAdmin(admin.ModelAdmin):
    list_display = ('codigo','logradouro')
    list_select_related = ('logradouro','logradouro__cidade')
    search_fields = ('codigo',)

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome','cnpj','cidade')
    list_select_related = ('cidade','cidade__estado')
    search_fields = ('nome','cnpj')
    list_filter = ('cidade__estado',)

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome','cpf','empresa','cargo','data_admissao')
    list_select_related = ('empresa','empresa__cidade')
    search_fields = ('nome','cpf','empresa__nome')
    list_filter = ('cargo',)
    raw_id_fields = ('empresa',)
