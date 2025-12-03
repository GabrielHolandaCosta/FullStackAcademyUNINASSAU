# Exercício 08 - Personalização do Django Admin

📅 **Entrega:** 26/10/2025 até às 23h59  
📚 Baseado na aula 9 do curso de Django.

---

## 📌 Descrição
O objetivo deste exercício foi personalizar o Django Admin e otimizar o desempenho do painel administrativo, minimizando as lentidões que ocorriam ao acessar algumas classes.

---

## 🛠️ Funcionalidades

### Personalizações Implementadas

1. **Templates Customizados**
   - `templates/admin/base.html`: Template base personalizado com AdminLTE
   - `templates/admin/custom_base_site.html`: Personalização do site admin
   - Modo escuro (dark mode) aplicado
   - Logo e branding personalizados

2. **Otimizações no Admin**
   - `list_select_related`: Reduz consultas ao banco de dados
   - `raw_id_fields`: Melhora performance em relacionamentos
   - `list_display`: Exibe campos relevantes
   - `search_fields`: Busca otimizada
   - `list_filter`: Filtros eficientes

3. **Classes Admin Otimizadas**
   - `EstadoAdmin`: list_display, search_fields
   - `CidadeAdmin`: list_select_related('estado'), list_filter
   - `LogradouroAdmin`: list_select_related('cidade', 'cidade__estado')
   - `CEPAdmin`: list_select_related('logradouro', 'logradouro__cidade')
   - `EmpresaAdmin`: list_select_related, list_filter por estado
   - `FuncionarioAdmin`: raw_id_fields('empresa'), list_select_related

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
pip install -r requirements.txt
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

5. Popular o banco de dados:
```bash
python script_popula_banco_estado_cidades_logradouro_cep.py
```

6. Rodar o servidor:
```bash
python manage.py runserver
```

7. Acessar o admin:
   - http://127.0.0.1:8000/admin

---

## 📝 Observações
- O admin foi reestilizado usando AdminLTE via CDN
- As otimizações reduzem significativamente a lentidão ao acessar classes com relacionamentos
- `select_related` evita consultas N+1 ao banco de dados
- `raw_id_fields` melhora a performance em campos ForeignKey com muitos registros
- O modo escuro foi aplicado para melhor experiência visual

---

## 🎯 Requisitos Atendidos
✅ Personalização do Django Admin implementada  
✅ Lentidões identificadas e minimizadas  
✅ Otimizações adicionadas nas classes do admin  
✅ Templates customizados aplicados  
✅ Branch criada para verificar alterações (feature/custom_admin)

---

## 🔧 Otimizações Aplicadas
- Uso de `list_select_related` para reduzir queries
- `raw_id_fields` em relacionamentos ForeignKey
- `search_fields` otimizados
- `list_filter` eficientes
- Templates personalizados com AdminLTE
