from datetime import timedelta, datetime
from aula.models import AulaDoAluno
from .models import Aluno

def alunos_nao_participantes_de_aula(id_aula):
    """
        Retorna uma lista de alunos que não estão na aula para não haver duplicação de AulaDoAluno.
    """
    alunos_participantes = AulaDoAluno.objects.filter(aula=id_aula).values_list('aluno', flat=True)
    return Aluno.objects.exclude(id__in=alunos_participantes)


def datas_recorrentes(data_inicio, data_fim, hora, intervalo):
    datas = []
    datas.append(datetime.combine(date = data_inicio, time=hora))
    while data_inicio <= data_fim:
        data_inicio += timedelta(days=intervalo)
        if not data_inicio > data_fim:
            datas.append(datetime.combine(date = data_inicio, time=hora))
    return datas

def media_criterios_avaliacao(avaliacoes):
    """
        Retorna a média dos critérios de avaliação de um aluno específico.
        Recebe as avaliações de um aluno como parâmetro.
    """
    qte_avaliacoes = avaliacoes.count()
    if qte_avaliacoes == 0:
        return None
    assiduidade = 0
    iniciativa = 0
    profissionalismo = 0
    raciocinio_clinico = 0
    relacao_med_paciente = 0
    for avaliacao in avaliacoes:
        assiduidade += avaliacao.checklist['assiduidade']
        iniciativa += avaliacao.checklist['iniciativa']
        profissionalismo += avaliacao.checklist['profissionalismo']
        raciocinio_clinico += avaliacao.checklist['raciocinio_clinico']
        relacao_med_paciente += avaliacao.checklist['relacao_med_paciente']

    return {
        'assiduidade': assiduidade / qte_avaliacoes,
        'iniciativa': iniciativa / qte_avaliacoes,
        'profissionalismo': profissionalismo / qte_avaliacoes,
        'raciocinio_clinico': raciocinio_clinico / qte_avaliacoes,
        'relacao_med_paciente': relacao_med_paciente / qte_avaliacoes,
    }
