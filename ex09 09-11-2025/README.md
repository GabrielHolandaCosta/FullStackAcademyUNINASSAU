# Exercício 09 - Django Rest Framework

## Entrega: 09/11/2025 até às 23h59min

Este projeto demonstra a criação de uma API REST usando Django Rest Framework.

## Estrutura do Projeto

- **App `usuarios`**: Gerencia usuários e perfis
- **App `gastos`**: Gerencia categorias e gastos

## Instalação

1. Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute as migrações:
```bash
python manage.py makemigrations
python manage.py migrate
```

4. Crie um superusuário:
```bash
python manage.py createsuperuser
```

5. Execute o servidor:
```bash
python manage.py runserver
```

## Endpoints da API

### Usuários
- `GET /api/usuarios/` - Lista todos os usuários
- `POST /api/usuarios/` - Cria um novo usuário
- `GET /api/usuarios/{id}/` - Detalhes de um usuário
- `PUT /api/usuarios/{id}/` - Atualiza um usuário (completo)
- `PATCH /api/usuarios/{id}/` - Atualiza um usuário (parcial)
- `DELETE /api/usuarios/{id}/` - Remove um usuário

### Perfis
- `GET /api/perfis/` - Lista todos os perfis
- `POST /api/perfis/` - Cria um novo perfil
- `GET /api/perfis/{id}/` - Detalhes de um perfil
- `PUT /api/perfis/{id}/` - Atualiza um perfil (completo)
- `PATCH /api/perfis/{id}/` - Atualiza um perfil (parcial)
- `DELETE /api/perfis/{id}/` - Remove um perfil

### Categorias de Gastos
- `GET /api/categorias/` - Lista todas as categorias
- `POST /api/categorias/` - Cria uma nova categoria
- `GET /api/categorias/{id}/` - Detalhes de uma categoria
- `PUT /api/categorias/{id}/` - Atualiza uma categoria (completo)
- `PATCH /api/categorias/{id}/` - Atualiza uma categoria (parcial)
- `DELETE /api/categorias/{id}/` - Remove uma categoria

### Gastos
- `GET /api/gastos/` - Lista todos os gastos do usuário logado
- `POST /api/gastos/` - Cria um novo gasto
- `GET /api/gastos/{id}/` - Detalhes de um gasto
- `PUT /api/gastos/{id}/` - Atualiza um gasto (completo)
- `PATCH /api/gastos/{id}/` - Atualiza um gasto (parcial)
- `DELETE /api/gastos/{id}/` - Remove um gasto

## Métodos HTTP Demonstrados

- **GET**: Listar e recuperar recursos
- **POST**: Criar novos recursos
- **PUT**: Atualizar recursos completamente
- **PATCH**: Atualizar recursos parcialmente
- **DELETE**: Remover recursos

## Tecnologias Utilizadas

- Django 5.0.1
- Django Rest Framework 3.14.0
- SQLite (banco de dados padrão)

## Acesso à Interface Web da API

Após iniciar o servidor, acesse:
- Interface web da API: http://127.0.0.1:8000/api/
- Admin do Django: http://127.0.0.1:8000/admin/

