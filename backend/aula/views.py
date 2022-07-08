from django.contrib.auth.decorators import permission_required
from users.utils import is_admin, listar_alunos
from django.shortcuts import redirect, render, get_object_or_404
from users.utils import is_admin
from users.models import Professor, Aluno
from turma.models import Turma
from avaliacao.models import Avaliacao
from .forms import AulaForm, AulaFormEdit, AulaDoAlunoForm
from .models import Aula, AulaDoAluno

class AulaTemplate:
    def index_aula_prof(request, username):
        prof = Professor.objects.get(user=request.user)
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
        #avaliacoes = []
        aula = get_object_or_404(Aula, pk=id)
        alunos = AulaDoAluno.objects.filter(aula=aula)
        # for aluno in alunos:
        #     avaliacoes.append(Avaliacao.objects.filter(aula_do_aluno=aluno))
        # avaliacoes_dos_alunos = zip(alunos, avaliacoes)
        context = {
            'full_name': request.user.get_full_name(),
            'aula': aula,
            'alunos': alunos,
            #'avaliacoes': avaliacoes,
            #'avaliacoes_dos_alunos': avaliacoes_dos_alunos,
        }
        context.update(is_admin(request))
        return render(request, 'aula/get_aula.html', context)

    @permission_required('aula.change_aula', login_url='/', raise_exception=True)
    def edit_aula(request, id):
        aula = Aula.objects.get(pk=id)
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
        aula = Aula.objects.get(pk=id)
        context = {
            'full_name': request.user.get_full_name(),
            'aula': aula,
        }
        context.update(is_admin(request))
        return render(request, 'aula/delete_aula.html', context)

    @permission_required('aula.delete_aula', login_url='/', raise_exception=True)
    def delete_aula(request, id):
        aula = Aula.objects.get(pk=id)
        aula.delete()
        return redirect('aula:index_aula_admin')

class AulaDoAlunoView():
    """
        CRUD para manter um aluno em uma aula
    """
    @permission_required('aula.add_auladoaluno', login_url='/', raise_exception=True)
    def add_aluno_em_aula(request, id_aula):
        aula = get_object_or_404(Aula, pk=id_aula)
        if request.method == 'POST':
            form = AulaDoAlunoForm(request.POST)
            if form.is_valid():
                id_alunos = form.cleaned_data['alunos']
                AulaDoAluno.objects.bulk_create(ignore_conflicts=False, objs = [
                    AulaDoAluno(aula=aula, aluno=Aluno.objects.get(pk=id)) for id in id_alunos
                ])
                return redirect('aula:get_aula', id_aula)
        else:
            form = AulaDoAlunoForm()
        context = listar_alunos(request)
        context.update({'aula':aula})
        context.update({'form':form})
        return render(request, 'aula_do_aluno/add_aluno_em_aula.html', context)

    @permission_required('aula.delete_auladoaluno', login_url='/', raise_exception=True)
    def remover_aluno_de_aula_template(request, id_aluno, id_aula):
        aula = get_object_or_404(AulaDoAluno, aula=id_aula, aluno=id_aluno)
        context = {
            'aula':aula,
            'full_name': request.user.get_full_name(),
            'is_admin': True,
        }
        return render(request, 'aula_do_aluno/remover_aluno_de_aula_template.html', context)

    @permission_required('aula.delete_auladoaluno', login_url='/', raise_exception=True)
    def remover_aluno_de_aula(request, id_aluno, id_aula):
        aula = get_object_or_404(AulaDoAluno, aula=id_aula, aluno=id_aluno)
        aula.delete()
        #msg successo
        return redirect("aula:get_aula", id_aula)
