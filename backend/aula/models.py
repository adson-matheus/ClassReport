from django.db import models
from users.models import Aluno
from disciplina.models import Disciplina

# Create your models here.
class Aula(models.Model):
    disciplina = models.ForeignKey(Disciplina, verbose_name="Disciplina", null=False, blank=False, on_delete=models.DO_NOTHING)
    assunto = models.CharField(verbose_name='Assunto da aula', max_length=255, null=False)
    datetime = models.DateTimeField(verbose_name='Data e Hora da Aula',auto_now=False, auto_now_add=False)

    class Meta:
        ordering = ('-datetime',)
    def __str__(self):
        return 'Assunto: {} - Prof. {}'.format(self.assunto, self.disciplina.idProfessor.user.get_full_name())

class AulaDoAluno(models.Model):
    aula = models.ForeignKey(Aula, verbose_name="Aula", on_delete=models.CASCADE, null=True)
    aluno = models.ForeignKey(Aluno, verbose_name="Aluno", on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ('-id',)
    def __str__(self):
        return '{} - {}'.format(self.idAluno, self.idAula)
