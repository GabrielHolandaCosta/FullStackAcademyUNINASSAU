# Exercício 06 - Django: Modelos Pessoa e Endereço + Perfil  
📅 Entrega: 05/10/2025 até às 23h59  
📚 Baseado nas aulas 8, 9 e 10 do curso de Django.  

---

## 📌 Descrição  
O objetivo deste exercício foi criar os modelos **Pessoa** e **Endereco**, registrar no Django Admin e exibir os dados de cada usuário em uma **página de perfil única** para todos os tipos de usuário.

- Pessoa vinculada a um usuário (`ForeignKey`)
- Pessoa vinculada a um endereço (`OneToOneField`)
- Endereço com rua, número, bairro, cidade, estado e cep

Todos os usuários (admin, gerente, usuário comum) acessam a mesma página de perfil.

---

## 🚀 Como executar  
1. Criar ambiente virtual e ativar  
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate # Linux/Mac
```
2. Instalar dependências  
```bash
pip install django
```
3. Rodar migrações  
```bash
python manage.py makemigrations
python manage.py migrate
```
4. Criar superusuário  
```bash
python manage.py createsuperuser
```
5. Rodar o servidor  
```bash
python manage.py runserver
```
6. Acessar a aplicação  
- Login: http://127.0.0.1:8000/login/  
- Perfil: http://127.0.0.1:8000/perfil/

---
