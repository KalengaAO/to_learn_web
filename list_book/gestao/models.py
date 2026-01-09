from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=200)
    idade = models.IntegerField(default=0)

    def __str__(self):
        return self.nome

class Book(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    editora = models.CharField(max_length=200)
    pagina = models.IntegerField(default=0)
    isbn = models.IntegerField(default=0)
    sinopse = models.TextField(max_length=400)

    def __str__(self):
        return self.titulo