# Exercício 02 - Django + Bootstrap

📅 **Entrega:** 07/09/2025 até às 23h59  
📚 Baseado nas aulas 5, 6 e 7 do curso de Django.

---

## 📌 Descrição
O objetivo deste exercício foi criar uma aplicação simples em **Django**, com uso de **Bootstrap** para o frontend.  

A aplicação implementa o cadastro e listagem de pessoas, com autenticação via tela de login.

---

## 🛠️ Funcionalidades

### Modelo Pessoa
- ✅ Nome
- ✅ CPF (único)
- ✅ E-mail
- ✅ Telefone
- ✅ Data de nascimento
- ✅ RG
- ✅ Endereço
- ✅ Bairro

### Funcionalidades Implementadas
- ✅ Registro do modelo no **Django Admin**
- ✅ **Tela de login** com autenticação
- ✅ Impressão de usuário e senha no terminal para fins de teste (DEBUG)
- ✅ **View + Template** para exibir a lista de pessoas cadastradas
- ✅ Layout responsivo com **Bootstrap 5.3**

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
   - Login: http://127.0.0.1:8000/login/
   - Lista de pessoas: http://127.0.0.1:8000/ (após login)
   - Admin: http://127.0.0.1:8000/admin/

---

## 📝 Observações
- A tela de login foi reaproveitada do exercício anterior (ex01)
- O sistema imprime no console do servidor o usuário e senha digitados (apenas para teste em desenvolvimento)
- Para adicionar pessoas, utilize o Django Admin
- A lista de pessoas é exibida em uma tabela Bootstrap
- O acesso à lista de pessoas requer autenticação

---

## 🎯 Requisitos Atendidos
✅ Modelo Pessoa criado com todos os atributos solicitados  
✅ Modelo registrado no Django Admin  
✅ View criada para acessar os dados  
✅ Template criado para exibição dos dados  
✅ Tela de login implementada (reaproveitada do ex01)  
✅ View de login imprime dados no prompt de comando para teste  
✅ Bootstrap utilizado em todas as telas

---

## 🔧 Tecnologias
- Django 5.0+
- Bootstrap 5.3.0
- Python 3.x
