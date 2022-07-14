from django.contrib.auth.decorators import permission_required
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from users.utils import is_admin
from avaliacao.utils import alunos_sem_avaliacao_da_aula
from .utils import alunos_nao_participantes_de_aula
from .models import Aula, AulaDoAluno
from .forms import AulaForm, AulaFormEdit, AulaDoAlunoForm
from turma.models import Turma
from users.models import Professor, Aluno

class AulaTemplate:
    def index_aula_prof(request, username):
        prof = get_object_or_404(Professor, user=request.user)
        context = {
            'queryset': Aula.objects.filter(turma__professor = prof),
            'username': username,
            'full_name': request.user.get_full_name(),
            'is_admin': False
        }
        return render(request, 'aula/index_aula_prof.html', context)

    def index_aula_admin(request):
        context = {
            'aulas': Aula.objects.all(),
            'username': request.user.get_username(),
            'full_name': request.user.get_full_name(),
            'is_admin': True
        }
        return render(request, 'aula/index_aula_admin.html', context)

    @permission_required('aula.add_aula', login_url='/', raise_exception=True)
    def add_aula(request):
        if request.method == 'POST':
            form_aula = AulaForm(request.POST)
            if form_aula.is_valid():
                form_aula.save()
                return redirect('aula:index_aula_admin')
            else:
                pass
                #message
        else:
            form_aula = AulaForm()
        context = {
            'form_aula': form_aula,
            'turmas': Turma.objects.all(),
            'full_name': request.user.get_full_name(),
        }
        context.update(is_admin(request))
        return render(request, 'aula/add_aula.html', context)

    def get_aula(request, id):
        aula = get_object_or_404(Aula, pk=id)
        context = {
            'full_name': request.user.get_full_name(),
            'aula': aula,
        }
        context.update(alunos_sem_avaliacao_da_aula(aula))
        context.update(is_admin(request))
        return render(request, 'aula/get_aula.html', context)

    @permission_required('aula.change_aula', login_url='/', raise_exception=True)
    def edit_aula(request, id):
        aula = get_object_or_404(Aula, pk=id)
        if request.method == 'POST':
            form_aula = AulaFormEdit(request.POST, instance=aula)
            if form_aula.is_valid():
                dados = form_aula.clean()
                turma = dados['turma']
                assunto = dados['assunto']
                datetime = dados['datetime']
                Aula(id=id, turma=turma, assunto=assunto, datetime=datetime).save()
                # msg
                return redirect('aula:get_aula', id)
            else:
                # msg
                return redirect('aula:index_aula_admin')
        else:
            form_aula = AulaFormEdit(instance=aula)
        context = {
            'form_aula': form_aula,
            'aula': aula,
            'turmas': Turma.objects.all(),
            'full_name': request.user.get_full_name(),
        }
        context.update(is_admin(request))
        return render(request, 'aula/edit_aula.html', context)

    @permission_required('aula.delete_aula', login_url='/', raise_exception=True)
    def delete_aula_template(request, id):
        aula = get_object_or_404(Aula, pk=id)
        context = {
            'full_name': request.user.get_full_name(),
            'aula': aula,
        }
        context.update(is_admin(request))
        return render(request, 'aula/delete_aula.html', context)

    @permission_required('aula.delete_aula', login_url='/', raise_exception=True)
    def delete_aula(request, id):
        aula = get_object_or_404(Aula, pk=id)
        aula.delete()
        return redirect('aula:index_aula_admin')

class AulaDoAlunoView():
    """
        CRUD para manter um aluno em uma aula
    """
    @permission_required('aula.add_auladoaluno', login_url='/', raise_exception=True)
    def add_aluno_em_aula(request, aula_id):
        aula = get_object_or_404(Aula, pk=aula_id)
        if request.method == 'POST':
            form = AulaDoAlunoForm(request.POST)
            if form.is_valid():
                id_alunos = form.cleaned_data['alunos']
                AulaDoAluno.objects.bulk_create(ignore_conflicts=False, objs = [
                    AulaDoAluno(aula=aula, aluno=Aluno.objects.get(pk=id)) for id in id_alunos
                ])
                messages.success(request, 'Aluno(s) adicionado(s) com sucesso!')
                return redirect('aula:get_aula', aula_id)
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
        return render(request, 'aula_do_aluno/add_aluno_em_aula.html', context)

    @permission_required('aula.view_auladoaluno', login_url='/', raise_exception=True)
    def aulas_do_aluno(request, matr):
        aluno = get_object_or_404(Aluno, matricula=matr)
        context = {
            'full_name': request.user.get_full_name(),
            'aluno': aluno,
            'aulas': AulaDoAluno.objects.filter(aluno=aluno)
        }
        context.update(is_admin(request))
        return render(request, 'aula_do_aluno/aulas_do_aluno.html', context)

    @permission_required('aula.delete_auladoaluno', login_url='/', raise_exception=True)
    def remover_aluno_de_aula_template(request, aluno_id, aula_id):
        aula = get_object_or_404(AulaDoAluno, aula=aula_id, aluno=aluno_id)
        context = {
            'aula':aula,
            'full_name': request.user.get_full_name(),
            'is_admin': True,
        }
        return render(request, 'aula_do_aluno/remover_aluno_de_aula_template.html', context)

    @permission_required('aula.delete_auladoaluno', login_url='/', raise_exception=True)
    def remover_aluno_de_aula(request, aluno_id, aula_id):
        aula = get_object_or_404(AulaDoAluno, aula=aula_id, aluno=aluno_id)
        aula.delete()
        messages.success(request, 'Aluno removido da aula com sucesso!')
        return redirect("aula:get_aula", aula_id)
