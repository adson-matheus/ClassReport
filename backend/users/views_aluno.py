from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import permission_required
from users.utils import is_admin, listar_alunos
from .models import Aluno
from .forms import AlunoForm, EditarAlunoForm
from django.contrib import messages

@permission_required('users.view_aluno', login_url='/', raise_exception=True)
def index_aluno(request):
    context = listar_alunos()
    context.update({"full_name": request.user.get_full_name()})
    context.update(is_admin(request))
    return render(request, 'users/aluno/listar_alunos.html', context)

@permission_required('users.add_aluno', login_url='/', raise_exception=True)
def adicionar_aluno(request):
    """
        Administrador adiciona aluno
    """
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            messages.success(request, "Aluno adicionado com sucesso!")
            form.save()
            return redirect('users:index_aluno')
        else:
            messages.error(request, "Erro ao cadastrar aluno")
    else:
        form = AlunoForm()
    context = {
        'form': form,
        'user': request.user,
        'full_name': request.user.get_full_name()
    }
    context.update(is_admin(request))
    return render(request, 'users/aluno/adicionar_aluno.html', context)

@permission_required('users.change_aluno', login_url='/', raise_exception=True)
def editar_aluno(request, matr):
    aluno = get_object_or_404(Aluno, matricula=matr)
    if request.method == 'POST':
        form = EditarAlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            messages.success(request, "Aluno editado com sucesso!")
            form.save()
            return redirect('users:index_aluno')
        else:
            messages.error(request, "Erro ao editar aluno")
    else:
        form = EditarAlunoForm(instance=aluno)
    context = {
        'aluno': aluno,
        'user': request.user,
        'full_name': request.user.get_full_name()
    }
    context.update(is_admin(request))
    return render(request, 'users/aluno/editar_aluno.html', context)

@permission_required('users.delete_aluno', login_url='/', raise_exception=True)
def deletar_aluno_template(request, matr):
    aluno = Aluno.objects.get(matricula=matr)
    context = {
        'full_name': request.user.get_full_name(),
        'aluno': aluno,
    }
    context.update(is_admin(request))
    return render(request, 'users/aluno/deletar_aluno.html', context)

@permission_required('users.delete_aluno', login_url='/', raise_exception=True)
def deletar_aluno(request, matr):
    aluno = get_object_or_404(Aluno, matricula=matr)
    aluno.delete()
    messages.success(request, "Aluno deletado com sucesso!")
    return redirect('users:index_aluno')
