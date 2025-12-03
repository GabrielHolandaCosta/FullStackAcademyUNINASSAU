# Exercício 05 - Redirecionamento por Tipo de Usuário (Django)

📅 **Entrega:** 05/10/2025 até às 23h59  
📚 Baseado no projeto gestao_empresa_django.

---

## 📌 Descrição
O objetivo deste exercício foi organizar o projeto para que o sistema redirecione cada usuário para sua página específica após o login, baseado no tipo de usuário.

---

## 🛠️ Funcionalidades

### Redirecionamento por Tipo de Usuário
- **Usuário Administrador** (is_superuser): Redirecionado para `/admin/`
- **Usuário Gerente** (is_staff): Redirecionado para `/gerencia/`
- **Usuário Comum**: Redirecionado para `/usuario-comum/`

### Páginas Criadas
1. **Página de Gerência** (`/gerencia/`)
   - Acessível apenas para usuários com permissão de staff
   - Interface com Bootstrap
   - Funcionalidades específicas para gerentes

2. **Página do Usuário Comum** (`/usuario-comum/`)
   - Acessível para usuários comuns
   - Interface com Bootstrap
   - Funcionalidades básicas

3. **Página de Perfil** (`/perfil/`)
   - Acessível para todos os tipos de usuário
   - Exibe dados da pessoa vinculada ao usuário

### View de Login Customizada
- `CustomLoginView` que herda de `LoginView`
- Validação do tipo de usuário após autenticação
- Redirecionamento automático baseado nas permissões

---

## 🚀 Como executar

1. Criar ambiente virtual e ativar:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

2. Instalar dependências:
```bash
pip install django
```

3. Rodar migrações:
```bash
python manage.py makemigrations
python manage.py migrate
```

4. Criar superusuário:
```bash
python manage.py createsuperuser
```

5. Criar usuários de teste:
   - Superusuário: `python manage.py createsuperuser` (is_superuser=True, is_staff=True)
   - Gerente: Criar no admin com `is_staff=True` e `is_superuser=False`
   - Usuário comum: Criar no admin com `is_staff=False` e `is_superuser=False`

6. Rodar o servidor:
```bash
python manage.py runserver
```

7. Acessar:
   - Login: http://127.0.0.1:8000/login/
   - Admin: http://127.0.0.1:8000/admin/
   - Gerência: http://127.0.0.1:8000/gerencia/ (após login como gerente)
   - Usuário Comum: http://127.0.0.1:8000/usuario-comum/ (após login como usuário comum)
   - Perfil: http://127.0.0.1:8000/perfil/

---

## 📝 Observações
- As validações são feitas no `views.py` através da view de login customizada
- Cada tipo de usuário tem sua própria página específica
- O redirecionamento acontece automaticamente após o login bem-sucedido
- Todas as páginas utilizam Bootstrap para estilização

---

## 🎯 Requisitos Atendidos
✅ Sistema organizado para redirecionar cada usuário para sua página específica  
✅ Usuário comum redirecionado para página específica  
✅ Usuário administrador redirecionado para admin  
✅ Usuário gerente redirecionado para página de gerência  
✅ Validações feitas no views.py
