from rest_framework import serializers
from .models import Comuna, Nacionalidad, Direccion, Autor, Bibloteca, Libro, Lector, Prestamo, TipoCategoria, Categoria # Importamos tu modelo real

class Comuna_Serializer(serializers.ModelSerializer):
   class Meta: 
        model= Comuna
        fields: '__all__'

class Nacionalidad_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Nacionalidad
        fields = '__all__'

class Direccion_Serializer(serializers.ModelSerializer):
   class Meta:
        model = Direccion
        fields = '__all__'

class Autor_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Autor  # Usamos tu modelo de biblioteca
        fields = '__all__'
class Bibloteca_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Bibloteca
        fields = '__all__'
class Libro_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = '__all__'
class Lector_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Lector
        fields = '__all__'
class Prestamo_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo  # Usamos tu modelo de biblioteca
        fields = '__all__'
class TipoCategoria_Serializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCategoria
        fields = '__all__'
class Categoria_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'