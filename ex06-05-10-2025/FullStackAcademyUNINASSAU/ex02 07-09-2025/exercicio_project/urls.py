from django.contrib import admin
from django.urls import path, include
from pessoas import views as pessoas_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', pessoas_views.login_view, name='login'),  # rota de login em /login/
    path('', include('pessoas.urls')),  # lista em raiz (/)
]
