from django.db import models
from users.models import Professor
from disciplina.models import Disciplina
from datetime import date

# Create your models here.
class Turma(models.Model):
    professor = models.OneToOneField(Professor, verbose_name="Professor", blank=False, null=False, on_delete=models.DO_NOTHING)
    disciplina = models.OneToOneField(Disciplina, verbose_name="Disciplina", blank=False, null=False, on_delete=models.DO_NOTHING)
    ano = models.IntegerField(verbose_name="Ano da Turma", blank=True, null=True, default=date.today().year)
    periodo = models.IntegerField(verbose_name="Período da Turma", blank=True, null=True, default=1)
