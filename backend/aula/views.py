from django.shortcuts import redirect, render
from users.models import Professor, Area
from .forms import AulaForm
from .models import Aula
from datetime import datetime
class AulaTemplate:
    def index(request, username):
        context = {
            #'queryset': Aula.objects.get('idProfessor = {}'.format(idProfessor)),
            'username': username,
            'full_name': request.user.get_full_name()
        }
        return render(request, 'aula/aulas.html', context)
    def add_aula(request, username):
        if request.method == 'POST':
            form_aula = AulaForm(request.POST)
            print(form_aula)
            if form_aula.is_valid():
                idArea = form_aula.cleaned_data['idArea']
                assunto = form_aula.cleaned_data['assunto']
                dataAula = form_aula.cleaned_data['dataAula']
                horario = form_aula.cleaned_data['horario']

                dt = datetime(year=dataAula.year,
                              month=dataAula.month,
                              day=dataAula.day,
                              hour=horario.hour,
                              minute=horario.minute)
                print(dt)

                Aula(idProfessor=Professor.objects.get(user=request.user), idArea=idArea, assunto=assunto, datetime=dt).save()
                return redirect('aulas:aulas', request.user.username)
            else:
                pass
                #message
        else:
            form_aula = AulaForm()
        context = {
            'form_aula':form_aula,
            'full_name': request.user.get_full_name(),
            'areas': Area.objects.all()
        }
        return render(request, 'aula/add_aula.html', context)
