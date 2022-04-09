from django.db import models

# Create your models here.
class administrador(models.Model):
    siape = models.CharField(verbose_name='siape', primary_key=True, max_length=20, null=False)
    nome = models.CharField(verbose_name='nome', max_length=100, null=False)
    usuario = models.CharField(verbose_name='usuario', max_length=20, null=False)
    senha = models.CharField(verbose_name='senha', max_length=20, null=False)