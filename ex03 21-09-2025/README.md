# Exercício 03 - Relacionamentos entre Classes (Django)

📅 **Entrega:** 21/09/2025 até às 23h59  
📚 Baseado na aula 8 do curso de Django.

---

## 📌 Descrição
O objetivo deste exercício foi implementar relacionamentos entre classes no Django, criando modelos com ForeignKey e OneToOneField.

---

## 🛠️ Funcionalidades

### Modelos Criados

1. **Pessoa**
   - Nome
   - Usuário (ForeignKey para User do Django)
   
2. **Endereco**
   - Rua
   - Número
   - Bairro
   - Cidade
   - Estado
   - CEP
   - Relacionamento OneToOne com Pessoa

### View e Template
- View que obtém os dados das pessoas cadastradas
- Passa informações de nome, usuário vinculado e endereço para o HTML
- Template `index.html` lista os dados obtidos na view

---

## 🚀 Como executar

1. Instalar dependências:
```bash
pip install django
```

2. Rodar migrações:
```bash
python manage.py makemigrations
python manage.py migrate
```

3. Criar superusuário:
```bash
python manage.py createsuperuser
```

4. Rodar o servidor:
```bash
python manage.py runserver
```

5. Acessar:
   - Admin: http://127.0.0.1:8000/admin/
   - Lista de pessoas: http://127.0.0.1:8000/

---

## 📝 Observações
- O modelo Pessoa está vinculado a um usuário através de ForeignKey
- O modelo Endereco está relacionado à Pessoa através de OneToOneField
- A view utiliza `select_related` para otimizar as consultas ao banco de dados

