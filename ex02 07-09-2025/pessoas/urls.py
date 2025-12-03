from django.urls import path
from . import views

app_name = 'pessoas'

urlpatterns = [
    path('', views.pessoa_list, name='list'),
    path('login/', views.login_view, name='login'),  # se quiser ter /pessoas/login/
]
