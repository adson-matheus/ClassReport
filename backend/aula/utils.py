from aula.models import AulaDoAluno
from .models import Aluno

def alunos_nao_participantes_de_aula(id_aula):
    """
        Retorna uma lista de alunos que não estão na aula para não haver duplicação de AulaDoAluno.
    """
    alunos_participantes = AulaDoAluno.objects.filter(aula=id_aula).values_list('aluno', flat=True)
    return Aluno.objects.exclude(id__in=alunos_participantes)
