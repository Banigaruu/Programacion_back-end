from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

# Registra todos los endpoints
router.register(r'comunas', views.ComunaViewSet)
router.register(r'nacionalidades', views.NacionalidadViewSet)
router.register(r'direcciones', views.DireccionViewSet)
router.register(r'autores', views.AutorViewSet)
router.register(r'bibliotecas', views.BiblotecaViewSet)
router.register(r'libros', views.LibroViewSet)
router.register(r'lectores', views.LectorViewSet)
router.register(r'prestamos', views.PrestamoViewSet)
router.register(r'tipo_categoria', views.TipoCategoriaViewSet)
router.register(r'categoria', views.CategoriaViewSet)

urlpatterns = [
    path('', include(router.urls))
]