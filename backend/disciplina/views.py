from disciplina.models import Disciplina
from disciplina.forms import DisciplinaForm, EditarDisciplinaForm
from django.shortcuts import render, redirect, get_object_or_404
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
    return render(request, 'disciplina/listar_disciplinas.html', context)

@permission_required('disciplina.add_disciplina', login_url='/', raise_exception=True)
def adicionar_disciplina(request):
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
    return render(request, 'disciplina/adicionar_disciplina.html', context)

@permission_required('disciplina.change_disciplina', login_url='/', raise_exception=True)
def editar_disciplina(request, id):
    disciplina = get_object_or_404(Disciplina, pk=id)
    if request.method == 'POST':
        form = EditarDisciplinaForm(request.POST, instance=disciplina)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            Disciplina(id=id, nome=nome).save()
            return redirect('disciplina:listar_disciplinas')
    else:
        form = EditarDisciplinaForm(instance=Disciplina)

    context = {
        'form': form,
        'disciplina': disciplina,
        'full_name': request.user.get_full_name(),
        'is_admin': True,
    }
    return render(request, 'disciplina/editar_disciplina.html', context)

@permission_required('disciplina.delete_disciplina', login_url='/', raise_exception=True)
def deletar_disciplina_template(request, id):
    disciplina = get_object_or_404(Disciplina, pk=id)
    context = {
        'full_name': request.user.get_full_name(),
        'disciplina': disciplina,
    }
    context.update(is_admin(request))
    return render(request, 'disciplina/deletar_disciplina.html', context)

@permission_required('disciplina.delete_disciplina', login_url='/', raise_exception=True)
def deletar_disciplina(request, id):
    disciplina = Disciplina.objects.get(pk=id)
    try:
        disciplina.delete()
        messages.success(request, '{} deletada com sucesso!'.format(disciplina))
        return redirect('disciplina:listar_disciplinas')

    except ProtectedError as e:
        turmas = [ turma.__str__() for turma in e.protected_objects ]
        messages.error(request, '{} não pode ser excluída. A(s) seguinte(s) turma(s) usa(m) essa disciplina: {}!'.format(disciplina, turmas))
        return redirect('disciplina:deletar_disciplina_template', disciplina.id)
