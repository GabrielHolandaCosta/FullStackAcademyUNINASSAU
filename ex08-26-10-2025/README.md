
Projeto: gestao_empresa_django (esqueleto para exercício de personalização do Django Admin)

Instruções rápidas:
1. Crie e ative um ambiente virtual (recomendado)
2. pip install -r requirements.txt
3. python manage.py makemigrations
4. python manage.py migrate
5. python manage.py createsuperuser
6. python script_popula_banco_estado_cidades_logradouro_cep.py
7. python manage.py runserver
8. Acesse o admin em http://127.0.0.1:8000/admin

O admin foi reestilizado usando AdminLTE via CDN em templates de admin (modo escuro).
Há otimizações em admin.py (list_display, select_related, search_fields) para reduzir lentidão.

Branch simulada: feature/custom_admin
