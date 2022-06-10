from django.contrib.auth.decorators import permission_required
from users.utils import is_admin, listar_alunos
from django.shortcuts import redirect, render, get_object_or_404
from users.utils import is_admin
from users.models import Professor
from turma.models import Turma
from users.models import Professor, Aluno
from .forms import AulaForm, AulaFormEdit
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
        aula = get_object_or_404(Aula, pk=id)
        context = {
            'full_name': request.user.get_full_name(),
            'aula': aula
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
    @permission_required('users.view_aluno', login_url='/', raise_exception=True)
    def index_alunos(request, id_aula):
        context = listar_alunos(request)
        aula = get_object_or_404(Aula, pk=id_aula)
        context.update({'aula':aula})
        return render(request, 'aula_do_aluno/index_alunos.html', context)

    @permission_required('aula.add_aula_do_aluno', login_url='/', raise_exception=True)
    def add_aluno_em_aula(request, id_aula, id_aluno):
        aula = Aula.objects.get(id=id_aula)
        aluno = Aluno.objects.get(id=id_aluno)
        #https://docs.djangoproject.com/en/4.0/ref/models/querysets/#bulk-create
        #bulk create
        AulaDoAluno(aula=aula, aluno=aluno).save()
        return render(request, 'aula_do_aluno/add_aluno_em_aula.html')
