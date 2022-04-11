from django.db import models

# Create your models here.
class Area(models.Model):
    nome = models.CharField(verbose_name='nome', primary_key=False, max_length=100, null=False)
    
    class Meta:
        ordering = ('-id',)
    def __str__(self):
        return self.nome

class Administrador(models.Model):
    siape = models.CharField(verbose_name='siape', primary_key=True, max_length=20, null=False)
    nome = models.CharField(verbose_name='nome', max_length=100, null=False)
    usuario = models.CharField(verbose_name='usuario', max_length=20, null=False)
    senha = models.CharField(verbose_name='senha', max_length=20, null=False)

    class Meta:
        ordering = ('-nome',)
    def __str__(self):
        return self.nome

class Aluno(models.Model):
    matricula = models.CharField(verbose_name='matricula', primary_key=True, max_length=20, null=False)
    nome = models.CharField(verbose_name='nome', primary_key=False, max_length=100, null=False)

    class Meta:
        ordering = ('-nome',)
    def __str__(self):
        return self.nome

class Professor(models.Model):
    siape = models.CharField(verbose_name='siape', primary_key=True, max_length=20, null=False)
    nome = models.CharField(verbose_name='nome', max_length=100, null=False)
    usuario = models.CharField(verbose_name='usuario', max_length=20, null=False)
    senha = models.CharField(verbose_name='senha', max_length=20, null=False)
    idArea = models.ForeignKey(Area, on_delete=models.CASCADE, null=False)

    class Meta:
        ordering = ('-nome',)
    def __str__(self):
        return self.nome
