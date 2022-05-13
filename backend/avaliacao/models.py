from django.db import models
from aula.models import AulaDoAluno, Aula
from users.models import Professor

# Create your models here.
class Avaliacao(models.Model):
    aula_do_aluno = models.ForeignKey(AulaDoAluno, on_delete=models.CASCADE, null=False)
    checklist = models.JSONField(verbose_name='checklist')

    class Meta:
        ordering = ('-id',)
    def __str__(self):
        return 'Avaliação da aula de {}'.format(self.aula_do_aluno)

class AvaliacoesProfessor(models.Model):
    id_avaliacao = models.ForeignKey(Avaliacao, on_delete=models.SET_NULL, null=False)
    id_professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=False)

    class Meta:
        ordering = ('-id',)
    def __str__(self):
        return 'Avaliação da aula de {}'.format(self.aula_do_aluno)
