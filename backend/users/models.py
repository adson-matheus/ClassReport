from django.db import models

# Create your models here.
class Administrador(models.Model):
    siape = models.CharField(verbose_name='siape', primary_key=True, max_length=20, null=False)
    nome = models.CharField(verbose_name='nome', max_length=100, null=False)
    usuario = models.CharField(verbose_name='usuario', max_length=20, null=False)
    senha = models.CharField(verbose_name='senha', max_length=20, null=False)

class Aluno(models.Model):
    matricula = models.CharField(verbose_name='matricula', primary_key=True, max_length=20, null=False)
    nome = models.CharField(verbose_name='nome', primary_key=False, max_length=100, null=False)

# class Professor(models.Model):
#     siape = models.CharField(verbose_name='siape', primary_key=True, max_length=20, null=False)
#     nome = models.CharField(verbose_name='nome', primary_key=False, max_length=100, null=False)
#     idArea = models.ForeignKey(Area, on_delete=models.CASCADE, on_update=models.CASCADE, null=False)
