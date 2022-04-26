from django.shortcuts import render
from .models import Aula

def crud_aula(request, username):
    context = {
        #'queryset': Aula.objects.get('idProfessor = {}'.format(idProfessor)),
        'username': request.user.username,
        'full_name': request.user.get_full_name()
    }
    return render(request, 'aula/aulas.html', context)
