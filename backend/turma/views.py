from django.shortcuts import render
from users.utils import is_admin
from .models import Turma

# Create your views here.
def listar_turmas(request):
    turmas = Turma.objects.all()
    context = {
        'turmas': turmas,
        'full_name': request.user.get_full_name(),
    }
    context.update(is_admin(request))
    return render(request, 'turma/listar_turmas.html', context)
