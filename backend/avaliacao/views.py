from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
from users.utils import is_admin
from .utils import json_para_string
from django.contrib import messages
from aula.models import AulaDoAluno
from .models import Avaliacao

# Create your views here.
def detalhar_avaliacao(request, id_aluno, id_aula):
    aula_do_aluno = get_object_or_404(AulaDoAluno, aluno=id_aluno, aula=id_aula)
    avaliacao = get_object_or_404(Avaliacao, aula_do_aluno=aula_do_aluno)
    str_avaliacao = json_para_string(avaliacao.checklist)
    context = {
        'full_name': request.user.get_full_name(),
        'avaliacao': avaliacao,
        'str_avaliacao': str_avaliacao,
    }
    context.update(is_admin(request))
    return render(request, 'avaliacao/detalhar_avaliacao.html', context)

@permission_required('avaliacao.delete_avaliacao', login_url='/', raise_exception=True)
def excluir_avaliacao_template(request, id_avaliacao):
    avaliacao = get_object_or_404(Avaliacao, pk=id_avaliacao)
    context = {
        'full_name': request.user.get_full_name(),
        'avaliacao': avaliacao,
    }
    context.update(is_admin(request))
    return render(request, 'avaliacao/excluir_avaliacao_template.html', context)

@permission_required('avaliacao.delete_avaliacao', login_url='/', raise_exception=True)
def excluir_avaliacao(request, id_avaliacao):
    avaliacao = get_object_or_404(Avaliacao, pk=id_avaliacao)
    avaliacao.delete()
    messages.success(request, f'Avaliação de {avaliacao.aula_do_aluno.aluno} excluída com sucesso!')
    return redirect('aula:get_aula', avaliacao.aula_do_aluno.aula.id)

def exportar_pdf(request, id_avaliacao):
    avaliacao = get_object_or_404(Avaliacao, pk=id_avaliacao)
    str_avaliacao = json_para_string(avaliacao.checklist)
    context = {
        'avaliacao': avaliacao,
        'str_avaliacao': str_avaliacao,
    }
    return render(request, 'avaliacao/exportar_pdf.html', context)
