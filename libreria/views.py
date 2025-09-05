from rest_framework import viewsets
from .serializer import (
    Comuna_Serializer, 
    Nacionalidad_Serializer,
    Direccion_Serializer,
    Autor_Serializer,
    Bibloteca_Serializer,
    Libro_Serializer,
    Lector_Serializer,
    Prestamo_Serializer,
    TipoCategoria_Serializer,
    Categoria_Serializer
)
from .models import (
    Comuna, 
    Nacionalidad,
    Direccion,
    Autor,
    Bibloteca,
    Libro,
    Lector,
    Prestamo,
    TipoCategoria,
    Categoria
)

# Create your views here.

class ComunaViewSet(viewsets.ModelViewSet):
    queryset = Comuna.objects.all()
    serializer_class = Comuna_Serializer

class NacionalidadViewSet(viewsets.ModelViewSet):
    queryset = Nacionalidad.objects.all()
    serializer_class = Nacionalidad_Serializer

class DireccionViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = Direccion_Serializer

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = Autor_Serializer

class BiblotecaViewSet(viewsets.ModelViewSet):
    queryset = Bibloteca.objects.all()
    serializer_class = Bibloteca_Serializer

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = Libro_Serializer

class LectorViewSet(viewsets.ModelViewSet):
    queryset = Lector.objects.all()
    serializer_class = Lector_Serializer

class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = Prestamo_Serializer

class TipoCategoriaViewSet(viewsets.ModelViewSet):
    queryset = TipoCategoria.objects.all()
    serializer_class = TipoCategoria_Serializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = Categoria_Serializer