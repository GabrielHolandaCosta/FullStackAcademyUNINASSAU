from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Pessoa

def login_view(request):
    """
    Recebe usuário e senha via POST, imprime no console (somente para teste DEV),
    tenta autenticar e redireciona para a lista se OK.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # DEBUG: imprime no console do servidor (apenas dev)
        print(f"[DEBUG LOGIN] username: {username} | password: {password}")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('pessoas:list')
        else:
            return render(request, 'login.html', {'error': 'Credenciais inválidas'})

    return render(request, 'login.html')


@login_required(login_url='/login/')
def pessoa_list(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'pessoas_list.html', {'pessoas': pessoas})
