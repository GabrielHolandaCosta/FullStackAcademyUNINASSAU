from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoriaGastoViewSet, GastoViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaGastoViewSet, basename='categoria')
router.register(r'gastos', GastoViewSet, basename='gasto')

urlpatterns = [
    path('', include(router.urls)),
]

