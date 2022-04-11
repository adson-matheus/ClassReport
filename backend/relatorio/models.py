from django.db import models
from users.models import Aluno, Administrador
from aula.models import Area, AulaDoAluno

# Create your models here.
class Avaliacao(models.Model):
    aula_do_aluno = models.ForeignKey(AulaDoAluno, on_delete=models.CASCADE, null=False)
    checklist = models.JSONField(verbose_name='checklist')

    class Meta:
        ordering = ('-id',)
    def __str__(self):
        return 'Avaliação da aula de {}'.format(self.aula_do_aluno)

class Relatorio(models.Model):
    idAdmin = models.ForeignKey(Administrador, verbose_name='Administrador', on_delete=models.CASCADE, null=False)
    idAvaliacao = models.ForeignKey(Avaliacao, verbose_name='Avaliacao', on_delete=models.CASCADE, null=False)
    idArea = models.ForeignKey(Area, verbose_name='Area', on_delete=models.CASCADE, null=False)
    relatorio = models.TextField(verbose_name='Relatório', max_length=2000, null=False)

    class Meta:
        ordering = ('-id',)
    def __str__(self):
        return 'Relatório de {} - {}'.format(self.idAdmin, self.idAvaliacao)

class AvaliacoesDoRelatorio(models.Model):
    idAvaliacao = models.ForeignKey(Avaliacao, on_delete=models.CASCADE, null=False)
    idRelatorio = models.ForeignKey(Relatorio, on_delete=models.CASCADE, null=False)
