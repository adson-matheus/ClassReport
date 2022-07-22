from django.db import models
from users.models import Aluno
from turma.models import Turma

# Create your models here.
class Aula(models.Model):
    turma = models.ForeignKey(Turma, verbose_name="Turma", null=True, blank=True, on_delete=models.PROTECT)
    assunto = models.CharField(verbose_name='Assunto da aula', max_length=255, null=True, blank=True)
    datetime = models.DateTimeField(verbose_name='Data e Hora da Aula', auto_now=False, auto_now_add=False)

    class Meta:
        ordering = ('datetime',)
    def __str__(self):
        return 'Turma: {}, Assunto: {}'.format(self.turma, self.assunto)

class AulaDoAluno(models.Model):
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE, null=False)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, null=False)

    class Meta:
        ordering = ('-id',)
    def __str__(self):
        return '{} - {}'.format(self.aluno, self.aula)
