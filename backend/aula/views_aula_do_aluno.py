from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.shortcuts import redirect, render, get_object_or_404
from django.db.models import Q
from users.utils import is_admin
from users.models import Aluno
from avaliacao.models import Avaliacao
from .utils import alunos_nao_participantes_de_aula, media_criterios_avaliacao
from .models import Aula, AulaDoAluno
from .forms import AulaDoAlunoForm
from datetime import datetime


class AulaDoAlunoView():
    """
        CRUD para manter um aluno em uma aula
    """
    @permission_required('aula.add_auladoaluno', login_url='/', raise_exception=True)
    def adicionar_aluno_em_aula(request, aula_id):
        aula = get_object_or_404(Aula, pk=aula_id)
        if request.method == 'POST':
            form = AulaDoAlunoForm(request.POST)
            if form.is_valid():
                id_alunos = form.cleaned_data['alunos']
                AulaDoAluno.objects.bulk_create(ignore_conflicts=False, objs = [
                    AulaDoAluno(aula=aula, aluno=Aluno.objects.get(pk=id)) for id in id_alunos
                ])
                messages.success(request, 'Aluno(s) adicionado(s) com sucesso!')
                return redirect('aula:detalhar_aula', aula_id)
            else:
                messages.error(request, 'Erro ao adicionar aluno(s)')
        else:
            form = AulaDoAlunoForm()
        context = {
            'full_name': request.user.get_full_name(),
            'aula':aula,
            'form': form,
        }
        context.update({'alunos': alunos_nao_participantes_de_aula(aula_id)})
        context.update(is_admin(request))
        return render(request, 'aula_do_aluno/adicionar_aluno_em_aula.html', context)

    @permission_required('aula.view_auladoaluno', login_url='/', raise_exception=True)
    def aulas_do_aluno(request, matr):
        aluno = get_object_or_404(Aluno, matricula=matr)
        data_inicio = request.GET.get('data_inicio')
        data_fim = request.GET.get('data_fim')
        if data_inicio and data_fim:
            aulas = AulaDoAluno.objects.filter(
                Q(aula__datetime__range=(data_inicio, data_fim)) |
                Q(aula__datetime__icontains=data_fim),
                aluno=aluno).order_by('aula__datetime')
            data_inicio = datetime.strptime(data_inicio, '%Y-%m-%d')
            data_fim = datetime.strptime(data_fim, '%Y-%m-%d')
        else:
            aulas = AulaDoAluno.objects.filter(aluno=aluno)
        aulas_id = [aula.aula.id for aula in aulas]
        avaliacoes = Avaliacao.objects.filter(aula_do_aluno__aula__in=aulas_id, aula_do_aluno__aluno=aluno)
        criterios_avaliacao = media_criterios_avaliacao(avaliacoes)
        presenca = aulas.filter(presenca=True).count()
        context = {
            'full_name': request.user.get_full_name(),
            'aluno': aluno,
            'aulas': aulas,
            'presenca': presenca,
            'data_inicio': data_inicio,
            'data_fim': data_fim,
            'avaliacoes': avaliacoes,
            'criterios_avaliacao': criterios_avaliacao,
        }
        context.update(is_admin(request))
        return render(request, 'aula_do_aluno/aulas_do_aluno.html', context)

    @permission_required('aula.delete_auladoaluno', login_url='/', raise_exception=True)
    def deletar_aluno_de_aula_template(request, aluno_id, aula_id):
        aula = get_object_or_404(AulaDoAluno, aula=aula_id, aluno=aluno_id)
        context = {
            'aula':aula,
            'full_name': request.user.get_full_name(),
            'is_admin': True,
        }
        return render(request, 'aula_do_aluno/deletar_aluno_de_aula_template.html', context)

    @permission_required('aula.delete_auladoaluno', login_url='/', raise_exception=True)
    def deletar_aluno_de_aula(request, aluno_id, aula_id):
        aula = get_object_or_404(AulaDoAluno, aula=aula_id, aluno=aluno_id)
        aula.delete()
        messages.success(request, 'Aluno removido da aula com sucesso!')
        return redirect("aula:detalhar_aula", aula_id)
