from disciplina.models import Disciplina
from disciplina.forms import DisciplinaForm, EditarDisciplinaForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from users.utils import is_admin
from django.db.models import ProtectedError
from django.contrib import messages

@permission_required('disciplina.view_disciplina', login_url='/', raise_exception=True)
def listar_disciplinas(request):
    context = {
        'disciplinas': Disciplina.objects.all(),
        'full_name': request.user.get_full_name(),
    }
    context.update(is_admin(request))
    return render(request, 'disciplina/disciplina.html', context)

@permission_required('disciplina.add_disciplina', login_url='/', raise_exception=True)
def add_disciplina(request):
    if request.method == 'POST':
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('disciplina:listar_disciplinas')
        else:
            pass
    else:
        form = DisciplinaForm()

    context = {
        'form': form,
        'full_name': request.user.get_full_name(),
        'is_admin': True,
    }
    return render(request, 'disciplina/add_disciplina.html', context)

@permission_required('disciplina.change_disciplina', login_url='/', raise_exception=True)
def editar_disciplina(request, id):
    if request.method == 'POST':
        form = EditarDisciplinaForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            Disciplina(id=id, nome=nome).save()
            return redirect('disciplina:listar_disciplinas')
    else:
        form = EditarDisciplinaForm()

    context = {
        'form': form,
        'disciplina': Disciplina.objects.get(pk=id),
        'full_name': request.user.get_full_name(),
        'is_admin': True,
    }
    return render(request, 'disciplina/editar_disciplina.html', context)

@permission_required('disciplina.delete_disciplina', login_url='/', raise_exception=True)
def excluir_disciplina_template(request, id):
    disciplina = Disciplina.objects.get(pk=id)
    context = {
        'full_name': request.user.get_full_name(),
        'disciplina': disciplina,
    }
    context.update(is_admin(request))
    return render(request, 'disciplina/excluir_disciplina.html', context)

@permission_required('disciplina.delete_disciplina', login_url='/', raise_exception=True)
def excluir_disciplina(request, id):
    disciplina = Disciplina.objects.get(pk=id)
    try:
        disciplina.delete()
        messages.success(request, '{} deletada com sucesso!'.format(disciplina))
        return redirect('disciplina:listar_disciplinas')

    except ProtectedError as e:
        turmas = [ turma.__str__() for turma in e.protected_objects ]
        messages.error(request, '{} não pode ser excluída. A(s) seguinte(s) turma(s) usa(m) essa disciplina: {}!'.format(disciplina, turmas))
        return redirect('disciplina:excluir_disciplina_template', disciplina.id)
