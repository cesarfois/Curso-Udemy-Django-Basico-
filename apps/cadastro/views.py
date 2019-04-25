from django.shortcuts import render

# Create your views here.
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
)

from .models import Autor, Libros

class ListaAutores(ListView):
    template_name = 'cadastro/lista-autores.html'
    model = Autor
    context_object_name = 'cadastro'

class ListaLibrosAutores(ListView):
    template_name = 'cadastro/lista-libros.html'
    context_object_name = 'libros'

    def get_queryset(self):
        # identificar o autor
        id = self.kwargs['pk']
        # filtro de los libros
        lista = Libros.objects.filter(
            autor=id
        )
        # devuelvo el resultado o la lista resultado
        return lista


class AddAutor(CreateView):
    # Vista para registrar um novo autor
    template_name = 'cadastro/add-autor.html'
    model = Autor
    fields = ['nome', 'telefone_residencial', 'email']
    success_url = '/'
