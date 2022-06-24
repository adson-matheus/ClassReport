from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
from users.utils import is_admin
from django.db.models import ProtectedError
from django.contrib import messages
from .models import Turma
from aula.models import Aula

@permission_required('turma.view_turma', login_url='/', raise_exception=True)
def listar_turmas(request):
    turmas = Turma.objects.all()
    context = {
        'turmas': turmas,
        'full_name': request.user.get_full_name(),
    }
    context.update(is_admin(request))
    return render(request, 'turma/listar_turmas.html', context)

@permission_required('turma.view_turma', login_url='/', raise_exception=True)
def listar_aulas_de_turma(request, id):
    turma = get_object_or_404(Turma, pk=id)
    aulas = Aula.objects.filter(turma=turma)
    context = {
        'aulas': aulas,
        'turma': turma,
        'full_name': request.user.get_full_name(),
    }
    context.update(is_admin(request))
    return render(request, 'turma/listar_aulas_de_turma.html', context)

@permission_required('turma.delete_turma', login_url='/', raise_exception=True)
def excluir_turma_template(request, id):
    turma = Turma.objects.get(pk=id)
    context = {
        'full_name': request.user.get_full_name(),
        'turma': turma,
    }
    context.update(is_admin(request))
    return render(request, 'turma/excluir_turma.html', context)

@permission_required('turma.delete_turma', login_url='/', raise_exception=True)
def excluir_turma(request, id):
    turma = get_object_or_404(Turma, pk=id)
    try:
        turma.delete()
        messages.success(request, '{} deletada com sucesso!'.format(turma))
        return redirect('turma:listar_turmas')

    except ProtectedError as e:
        for aula in e.protected_objects:
            messages.error(request, "Não é possível excluir a turma {}. A aula '{}' está cadastrada e faz parte desta turma!".format(turma, aula.assunto))
        return redirect('turma:excluir_turma_template', id)
