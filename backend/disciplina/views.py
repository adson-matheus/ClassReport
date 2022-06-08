from django.shortcuts import render
from disciplina.models import Disciplina
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
