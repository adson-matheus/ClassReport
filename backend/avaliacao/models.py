from django.db import models
from aula.models import AulaDoAluno, Aula
from users.models import Professor

# Create your models here.
class Avaliacao(models.Model):
    def default_checklist(**args):
        return {
            'assiduidade': args.get('assiduidade') or 2,
            'iniciativa': args.get('iniciativa') or 2,
            'profissionalismo': args.get('profissionalismo') or 2,
            'raciocinio_clinico': args.get('raciocinio_clinico') or 2,
            'relacao_med_paciente': args.get('relacao_med_paciente') or 2,
        }

    aula_do_aluno = models.OneToOneField(AulaDoAluno, on_delete=models.CASCADE, null=False)
    checklist = models.JSONField(verbose_name='checklist', default=default_checklist)

    class Meta:
        ordering = ('-id',)
    def __str__(self):
        return 'Avaliação da aula de {}'.format(self.aula_do_aluno)

class AvaliacoesProfessor(models.Model):
    id_avaliacao = models.ForeignKey(Avaliacao, on_delete=models.SET_NULL, null=True)
    id_professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ('-id',)
    def __str__(self):
        return 'Avaliação da aula de {}'.format(self.aula_do_aluno)
