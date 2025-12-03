from django.contrib import admin
from .models import CategoriaGasto, Gasto


@admin.register(CategoriaGasto)
class CategoriaGastoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    search_fields = ('nome',)


@admin.register(Gasto)
class GastoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'valor', 'categoria', 'usuario', 'data')
    list_filter = ('categoria', 'data', 'usuario')
    search_fields = ('descricao', 'usuario__username')
    date_hierarchy = 'data'

