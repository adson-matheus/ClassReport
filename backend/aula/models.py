from django.db import models
from users.models import Aluno

# Create your models here.
class Area(models.Model):
    nome = models.CharField(verbose_name='nome', primary_key=False, max_length=100, null=False)

class Aula(models.Model):
    idArea = models.ForeignKey(Area, on_delete=models.CASCADE, on_update=models.CASCADE, null=False)
    datetime = models.DateTimeField(auto_now=False, auto_now_add=False)

class AulaDoAluno(models.Model):
    idAula = models.ForeignKey(Aula, on_delete=models.CASCADE, on_update=models.CASCADE, null=False)
    idAluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, on_update=models.CASCADE, null=False)