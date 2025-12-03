from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from .models import Pessoa

class CustomLoginView(LoginView):
    template_name = 'login.html'
    
    def form_valid(self, form):
        """Redireciona cada tipo de usuário para sua página específica"""
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(self.request, user)
            
            # Verifica se é superusuário (administrador)
            if user.is_superuser:
                return redirect('admin:index')
            # Verifica se é staff (gerente)
            elif user.is_staff:
                return redirect('gerencia')
            # Usuário comum
            else:
                return redirect('usuario_comum')
        
        return super().form_valid(form)

@login_required
def perfil(request):
    try:
        pessoa = Pessoa.objects.get(usuario=request.user)
    except Pessoa.DoesNotExist:
        pessoa = None

    return render(request, 'perfil.html', {'pessoa': pessoa})

@login_required
def gerencia(request):
    """Página específica para gerentes"""
    return render(request, 'gerencia.html')

@login_required
def usuario_comum(request):
    """Página específica para usuários comuns"""
    return render(request, 'usuario_comum.html')
