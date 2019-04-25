from django.db import models

# Create your models here.

class Autor(models.Model):
    nome = models.CharField('nome',max_length=80)
    telefone_residencial = models.CharField(blank=True, max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Libros(models.Model):
    title = models.CharField('Titulo', blank=False, max_length=150)
    resume = models.TextField('Resume', blank=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
