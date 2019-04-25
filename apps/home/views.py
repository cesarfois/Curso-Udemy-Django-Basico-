from django.shortcuts import render

# Create your views here.
from django.views.generic import (
    TemplateView,
    ListView
)


class IndexView(TemplateView):
    # una vista processa los datos y renderiza el resultado en pantalla
    # siempre nos pedira un template con el que trabajar
    # un template es un archivo html
    # template_name etiqueta
    template_name = 'home/index.html'

class ListaLibros(ListView):
    template_name = 'home/lista.html'
    queryset = ['libro 1', 'libro 22', 'libro 333', 'django 2.0']
    context_object_name = 'libros'
