from django.contrib.auth.models import AbstractUser
from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Curso"

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Categoria"

class Professor(models.Model):
    nome = models.CharField(max_length=70)
    matricula = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Professor"

class Trabalho(models.Model):
    titulo = models.CharField(max_length=70)
    descricao = models.TextField(verbose_name='Descrição', null=True, blank=True)
    date = models.DateField(("Date de Cadastro"), auto_now=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoria',null=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name='Curso', null=True)
    professores = models.ManyToManyField(Professor)
    ano = models.IntegerField()

    def __str__(self):
        return self.nome