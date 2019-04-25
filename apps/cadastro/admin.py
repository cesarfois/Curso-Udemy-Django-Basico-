from django.contrib import admin

# Register your models here.
from . models import Autor, Libros

#clase para mostrar mais atributos no administrador.


class AutorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nome',
        'telefone_residencial',
        'email'
    )
    # Atributo para buscar por un campo
    search_fields = ('nome','email')


class LibrosAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'autor'
    )
    # Atributo para buscar por un campo
    search_fields = ('title',)
    # para hacer filtros
    list_filter = ('autor',)


admin.site.register(Autor,AutorAdmin)
admin.site.register(Libros, LibrosAdmin)