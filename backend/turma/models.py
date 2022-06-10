from django.db import models
from users.models import Professor
from disciplina.models import Disciplina
from datetime import date

# Create your models here.
class Turma(models.Model):
    professor = models.ForeignKey(Professor, verbose_name="Professor", blank=False, null=False, on_delete=models.PROTECT)
    disciplina = models.ForeignKey(Disciplina, verbose_name="Disciplina", blank=False, null=False, on_delete=models.PROTECT)
    ano = models.IntegerField(verbose_name="Ano da Turma", blank=True, null=True, default=date.today().year)
    periodo = models.IntegerField(verbose_name="Período da Turma", blank=True, null=True, default=1)
    descricao = models.CharField(verbose_name="Descrição, Código...", max_length=255, null=True, blank=True)

    class Meta:
        ordering = ('-disciplina',)
    def __str__(self):
        return '{} - {}.{} - {}'.format(self.disciplina, self.ano, self.periodo, self.professor.user.get_full_name())
