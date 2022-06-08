from disciplina.models import Disciplina
from disciplina.forms import DisciplinaForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from users.utils import is_admin

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
