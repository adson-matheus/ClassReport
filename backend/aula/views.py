from django.contrib.auth.decorators import permission_required
from django.shortcuts import redirect, render, get_object_or_404
from users.utils import is_admin
from avaliacao.utils import alunos_sem_avaliacao_da_aula
from django.contrib import messages
from .utils import datas_recorrentes
from .models import Aula
from .forms import AulaForm, AulaFormEdit, AulasRecorrentesForm
from turma.models import Turma
from users.models import Professor

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
                messages.success(request, 'Aula cadastrada com sucesso!')
                return redirect('aula:index_aula_admin')
            else:
                messages.error(request, 'Erro ao cadastrar aula!')
        else:
            form_aula = AulaForm()
        context = {
            'form_aula': form_aula,
            'turmas': Turma.objects.all(),
            'full_name': request.user.get_full_name(),
        }
        context.update(is_admin(request))
        return render(request, 'aula/add_aula.html', context)

    @permission_required('aula.add_aula', login_url='/', raise_exception=True)
    def add_aulas_recorrentes(request, turma_id):
        turma = get_object_or_404(Turma, id=turma_id)
        if request.method == 'POST':
            form_aula = AulasRecorrentesForm(request.POST)
            print(form_aula)
            if form_aula.is_valid():
                assunto = form_aula.cleaned_data['assunto']
                data_inicio = form_aula.cleaned_data['data_inicio']
                data_fim = form_aula.cleaned_data['data_fim']
                hora = form_aula.cleaned_data['hora']
                intervalo = form_aula.cleaned_data['intervalo']

                datas = datas_recorrentes(data_inicio=data_inicio, data_fim=data_fim, hora=hora, intervalo=intervalo)
                Aula.objects.bulk_create(objs = [ Aula(turma=turma, datetime=data, assunto=assunto) for data in datas ])
                messages.success(request, 'Aulas cadastradas com sucesso!')
                return redirect('turma:listar_aulas_de_turma', turma_id)
            else:
                messages.error(request, 'Erro ao cadastrar aulas!')
        else:
            form_aula = AulasRecorrentesForm()
        context = {
            'form_aula': form_aula,
            'full_name': request.user.get_full_name(),
            'turma': turma,
        }
        context.update(is_admin(request))
        return render(request, 'aula/add_aulas_recorrentes.html', context)


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
                messages.success(request, 'Aula editada com sucesso!')
                Aula(id=id, turma=turma, assunto=assunto, datetime=datetime).save()
                return redirect('aula:get_aula', id)
            else:
                messages.error(request, 'Erro ao editar aula!')
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
        messages.success(request, 'Aula deletada com sucesso!')
        return redirect('aula:index_aula_admin')

