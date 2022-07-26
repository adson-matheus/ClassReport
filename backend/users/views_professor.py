from django.shortcuts import get_object_or_404, redirect, render
from users.utils import is_admin
from .models import Professor
from django.contrib import messages

def index_professor(request):
    context = {
        'professores': Professor.objects.exclude(user__is_active=False),
        'full_name': request.user.get_full_name(),
        'is_admin': True,
    }
    return render(request, 'users/prof/professores.html', context)

def deletar_professor_template(request, siape):
    professor = get_object_or_404(Professor, siape=siape)
    context = {
        'full_name': request.user.get_full_name(),
        'professor': professor,
    }
    context.update(is_admin(request))
    return render(request, 'users/prof/deletar_professor.html', context)

def deletar_professor(request, siape):
    professor = get_object_or_404(Professor, siape=siape)
    professor.user.is_active = False
    professor.user.save()
    messages.success(request, "{} excluído com sucesso!".format(professor))
    return redirect('users:index_prof')
