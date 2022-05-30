from django.contrib.auth.models import Group
from .models import Aluno

def is_admin(request):
    group = Group.objects.get(name='grp_administradores')
    if group in request.user.groups.all():
        return {'is_admin':True}
    else: return {'is_admin':False}

def listar_alunos(request):
    alunos = Aluno.objects.all()
    context = {
        'alunos': alunos,
        'full_name': request.user.get_full_name()
    }
    context.update(is_admin(request))
    return context
