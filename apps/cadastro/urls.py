from django.urls import path, re_path, include

from . import views

app_name = 'cadastro_app'

urlpatterns = [
    path('', views.ListaAutores.as_view(), name='lista-autores'),
    path('autor/add', views.AddAutor.as_view(), name='add-autor'),
    path('libros-autor/<pk>/por-autor', views.ListaLibrosAutores.as_view(), name='lista-libros'),
]
