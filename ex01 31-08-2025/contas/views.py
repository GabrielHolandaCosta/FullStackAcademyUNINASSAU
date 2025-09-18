# contas/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'contas/home.html')

def cadastro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso! Faça seu login.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'contas/cadastro.html', {'form': form})

@login_required
def perfil(request):
    return render(request, 'contas/perfil.html')