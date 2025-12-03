# Exercício 01 - Telas de Autenticação e Erros (Django + Bootstrap)

📅 **Entrega:** 31/08/2025 até às 23h59  
📚 Exercício prático da disciplina de Full Stack Development (UNINASSAU).

---

## 📌 Descrição
O objetivo deste exercício foi desenvolver diversas telas em **Django** com estilização em **Bootstrap**, cobrindo autenticação de usuário e páginas de erro personalizadas.

---

## 🛠️ Funcionalidades

### Telas de Autenticação
1. ✅ **Tela de Login** com Bootstrap
   - Formulário de autenticação
   - Link para recuperação de senha
   - Link para cadastro

2. ✅ **Tela de Logout**
   - Confirmação de logout
   - Link para fazer login novamente

3. ✅ **Tela de Recuperar Senha**
   - Formulário para solicitar recuperação
   - Envio de instruções por e-mail
   - Confirmação de envio

4. ✅ **Tela de Alterar Senha**
   - Formulário para alterar senha atual
   - Validação de senha antiga
   - Confirmação de alteração

5. ✅ **Tela de Cadastro**
   - Formulário de criação de conta
   - Validação de dados
   - Redirecionamento para login após cadastro

6. ✅ **Tela de Perfil**
   - Exibição de dados do usuário
   - Link para alterar senha
   - Informações do usuário logado

7. ✅ **Tela Home**
   - Página inicial do sistema
   - Diferenciação entre usuário logado e não logado
   - Links para login e cadastro

### Páginas de Erro
8. ✅ **Página 404** - Página não encontrada
   - Design com Bootstrap
   - Link para voltar à home

9. ✅ **Página 403** - Acesso não permitido
   - Design com Bootstrap
   - Mensagem de acesso negado

10. ✅ **Página 500** - Erro no servidor
    - Design com Bootstrap
    - Mensagem de erro interno

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

5. Rodar o servidor:
```bash
python manage.py runserver
```

6. Acessar a aplicação:
   - Home: http://127.0.0.1:8000/
   - Login: http://127.0.0.1:8000/contas/login/
   - Cadastro: http://127.0.0.1:8000/cadastro/
   - Recuperar senha: http://127.0.0.1:8000/contas/password_reset/
   - Admin: http://127.0.0.1:8000/admin/

---

## 📝 Observações
- Todas as telas utilizam Bootstrap 5.3 para estilização
- O projeto está configurado com `DEBUG = False` para exibir as páginas de erro personalizadas
- As rotas de autenticação utilizam `django.contrib.auth.urls`
- O sistema de recuperação de senha está configurado para enviar e-mails no console (modo desenvolvimento)
- Todas as páginas são responsivas e seguem um design moderno

---

## 🎯 Requisitos Atendidos
✅ Tela de Login com Bootstrap  
✅ Tela de Logout com Bootstrap  
✅ Tela de Recuperar Senha com Bootstrap  
✅ Tela de Alterar Senha com Bootstrap  
✅ Tela de Cadastrar com Bootstrap  
✅ Tela de Perfil com Bootstrap  
✅ Tela Home com Bootstrap  
✅ Página de erro 404  
✅ Página de erro 403  
✅ Página de erro 500  
✅ Todas as rotas configuradas corretamente

---

## 🔧 Tecnologias
- Django 5.0+
- Bootstrap 5.3.3
- Font Awesome 5.15.4
- Python 3.x
