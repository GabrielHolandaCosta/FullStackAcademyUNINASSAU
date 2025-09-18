from django.shortcuts import render
from .models import Pessoa

def index(request):
    pessoas = Pessoa.objects.select_related('usuario', 'endereco').all()
    return render(request, 'index.html', {'pessoas': pessoas})
