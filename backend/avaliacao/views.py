from django.shortcuts import render, get_object_or_404
from users.utils import is_admin
from .utils import json_para_string
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
