from django.db import models
from users.models import Professor

# Create your models here.
class Disciplina(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=255, null=True, blank=True)
    idProfessor = models.ForeignKey(Professor, verbose_name="Professor", on_delete=models.SET_NULL, blank=True, null=True)
