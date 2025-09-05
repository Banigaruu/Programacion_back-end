from django.db import models

# Create your models here.
class Nacionalidad(models.Model):
    pais = models.CharField(max_length=50, null=False)
    Nacionalidad = models.CharField(max_length=50, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Autor(models.Model):
    nombre = models.CharField(max_length=250, null=False)
    pseudonimo = models.CharField(max_length=50, null=True)
    id_nacimiento = models.ForeignKey(Nacionalidad, on_delete=models.CASCADE)
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comuna(models.Model):
    codigo = models.CharField(max_length=5, null=False)
    Comuna = models.CharField(max_length=50, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Direccion(models.Model):
    id_comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    calle = models.CharField(max_length=50, null=True)
    numero = models.CharField(max_length=10, null=True)
    departamento = models.CharField(max_length=10, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Bibloteca(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    Direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Libro(models.Model):
    id_bibloteca = models.ForeignKey(Bibloteca, on_delete=models.CASCADE)
    genero = models.CharField(max_length=50, null=False)
    titulo = models.CharField(max_length=250, null=False)
    id_autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    paginas = models.IntegerField()
    copias = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Lector(models.Model):
    nombre = models.CharField(max_length=150, null=False)
    rut = models.IntegerField(null=False)
    digito_verificador = models.CharField(max_length=1, null=False)
    correo = models.CharField(max_length=50, null=True)
    telefono = models.CharField(max_length=20, null=False)
    Direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Prestamo(models.Model):
    id_libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    id_lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField(null=False)
    fecha_devolucion = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class TipoCategoria(models.Model):
    tipo_categoria = models.CharField(max_length=50, null=False)
    habilitado= models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Categoria(models.Model):
    id_tipo_categoria= models.ForeignKey(
        TipoCategoria, on_delete=models.CASCADE, null=False)
    categoria = models.CharField(max_length=100, null= False)
    descripcion = models.CharField(max_length=255, null=False)
    habilitado = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
