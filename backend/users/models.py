from django.db import models
from django.contrib.auth.models import User

class Aluno(models.Model):
    matricula = models.CharField(verbose_name='matricula', max_length=20, null=False, unique=True)
    nome = models.CharField(verbose_name='nome', max_length=100, null=False)

    class Meta:
        ordering = ('-nome',)
    def __str__(self):
        return self.nome

class Administrador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    siape = models.CharField(verbose_name='siape', primary_key=True, max_length=20, null=False)

    class Meta:
        ordering = ('-user',)
    def __str__(self):
        return self.user.get_full_name()

class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    siape = models.CharField(verbose_name='siape', primary_key=True, max_length=20, null=False)

    class Meta:
        ordering = ('-user',)
    def __str__(self):
        return self.user.get_full_name()
