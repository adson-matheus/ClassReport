from django.db import models
from users.models import Professor, Aluno, Area

# Create your models here.
class Aula(models.Model):
    idArea = models.ForeignKey(Area, on_delete=models.CASCADE, null=False)
    idProfessor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    assunto = models.CharField(verbose_name='Assunto da aula', max_length=50, null=False)
    datetime = models.DateTimeField(auto_now=False, auto_now_add=False)

    class Meta:
        ordering = ('-id',)
    def __str__(self):
        return '[{}] Aula: {} - Prof. {}, Área {}'.format(self.datetime, self.assunto, self.idProfessor, self.idArea)


class AulaDoAluno(models.Model):
    idAula = models.ForeignKey(Aula, on_delete=models.CASCADE, null=False)
    idAluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, null=False)

    class Meta:
        ordering = ('-id',)
    def __str__(self):
        return '{} - {}'.format(self.idAluno, self.idAula)