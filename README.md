# FullStack Academy - UNINASSAU

Repositório criado para armazenar os exercícios e projetos desenvolvidos durante a disciplina de **Full Stack Development (UNINASSAU)**.

Aqui você encontrará a evolução dos estudos em **Frontend (HTML, CSS, JavaScript, Bootstrap, Vue.js)** e **Backend (Python, Django, Django Rest Framework)**.

---

## 📂 Estrutura de Exercícios

### **ex01 31-08-2025** → Telas de autenticação e páginas de erro com Django + Bootstrap
- ✅ Login
- ✅ Logout
- ✅ Recuperar senha
- ✅ Alterar senha
- ✅ Cadastro
- ✅ Perfil
- ✅ Home
- ✅ Página de erro 404 (não encontrada)
- ✅ Página de erro 403 (não permitida)
- ✅ Página de erro 500 (erro interno no servidor)

### **ex02 07-09-2025** → CRUD simples com Django + Bootstrap
- ✅ Modelo `Pessoa` (Nome, CPF, E-mail, Telefone, Data de Nascimento, RG, Endereço, Bairro)
- ✅ Registro no Admin
- ✅ Tela de login (reaproveitada do ex01)
- ✅ Listagem de pessoas no template com Bootstrap
- ✅ View que imprime usuário e senha no terminal para teste

### **ex03 21-09-2025** → Relacionamentos entre classes no Django
- ✅ Modelo `Pessoa` vinculado a `User` (ForeignKey)
- ✅ Modelo `Endereco` relacionado a `Pessoa` (OneToOneField)
- ✅ View que obtém dados das pessoas com usuário e endereço
- ✅ Template listando nome, usuário e endereço

### **ex04 21-09-2025** → Página de vendas com Vue.js
- ✅ Diretivas `v-if`, `v-show`, `v-for`, `v-on`, `v-bind`
- ✅ Exibição de produtos e valores
- ✅ Adição de itens ao carrinho
- ✅ Exibição da opção de pagamento somente se houver itens no carrinho

### **ex05-05-10-2025** → Redirecionamento por tipo de usuário
- ✅ View de login customizada
- ✅ Redirecionamento para Administrador → `/admin/`
- ✅ Redirecionamento para Gerente → `/gerencia/`
- ✅ Redirecionamento para Usuário Comum → `/usuario-comum/`
- ✅ Validações feitas no `views.py`

### **ex06-05-10-2025** → Modelos Pessoa e Endereço + Perfil
- ✅ Modelo `Pessoa` com todos os atributos (Nome, CPF, E-mail, Telefone, Data de nascimento, RG)
- ✅ Modelo `Pessoa` com ForeignKey para User
- ✅ Modelo `Endereco` (rua, numero, bairro, cidade, estado, cep)
- ✅ Relacionamento Pessoa com Endereço
- ✅ Registro no Django Admin
- ✅ Página de perfil única para todos os tipos de usuário

### **ex07-15-10-2025** → Interpolação de texto e diretivas Vue.js
- ✅ Interpolação de texto com `{{ }}`
- ✅ Todas as diretivas Vue.js (v-if, v-show, v-for, v-on, v-bind, v-model)
- ✅ Dados de exemplo alterados
- ✅ Verificação com biblioteca Vetur

### **ex08-26-10-2025** → Personalização do Django Admin
- ✅ Templates customizados (AdminLTE)
- ✅ Otimizações para reduzir lentidão
- ✅ `list_select_related` em classes admin
- ✅ `raw_id_fields` em relacionamentos
- ✅ Modo escuro aplicado

### **ex09 09-11-2025** → Django Rest Framework
- ✅ Projeto Django Rest Framework completo
- ✅ App `usuarios` para gerenciar usuários
- ✅ App `gastos` para gerenciar gastos
- ✅ ModelViewSets implementados
- ✅ Serializers configurados
- ✅ Routers configurados
- ✅ Todos os métodos HTTP (GET, POST, PUT, PATCH, DELETE)

---

## 🚀 Tecnologias utilizadas
- Python 3.x
- Django 5.0+
- Django Rest Framework 3.14+
- Bootstrap 5.3+
- HTML, CSS e JavaScript
- Vue.js 2.6+ / 3.x
- Git e GitHub

---

## 🎯 Objetivo do Repositório
Centralizar todos os exercícios práticos da disciplina, para fins de estudo, acompanhamento e evolução no desenvolvimento **Full Stack**.

---

## 📚 Como usar este repositório

Cada exercício possui seu próprio diretório com:
- Código fonte completo
- README.md com instruções específicas
- Requisitos e dependências (quando aplicável)
- Instruções de instalação e execução

Para executar um exercício específico, navegue até o diretório do exercício e siga as instruções no README.md correspondente.

---

## 👨‍💻 Autor
**Gabriel Holanda**  
Desenvolvido durante o curso de Full Stack Development na UNINASSAU.

---

## 📝 Licença
Este repositório é para fins educacionais.
