from django.contrib import admin
from .models import Nacionalidad, Autor, Comuna, Direccion, Bibloteca, Lector, Libro, Prestamo, TipoCategoria, Categoria
# Register your models here.
admin.site.register(Nacionalidad)
admin.site.register(Autor)
admin.site.register(Comuna)
admin.site.register(Direccion)
admin.site.register(Bibloteca)
admin.site.register(Lector)
admin.site.register(Libro)
admin.site.register(Prestamo)
admin.site.register(TipoCategoria)
admin.site.register(Categoria)