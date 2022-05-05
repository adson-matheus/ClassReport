from django.shortcuts import redirect, render
from .utils import converter_para_datetime
from users.models import Professor, Area
from .forms import AulaForm, AulaFormEdit
from .models import Aula
from datetime import datetime

class AulaTemplate:
    def index_aula(request, username):
        prof = Professor.objects.get(user=request.user)
        context = {
            'queryset': Aula.objects.filter(idProfessor = prof),
            'username': username,
            'full_name': request.user.get_full_name()
        }
        return render(request, 'aula/aulas.html', context)
    def add_aula(request, username):
        if request.method == 'POST':
            form_aula = AulaForm(request.POST)
            if form_aula.is_valid():
                dados = form_aula.clean()
                idArea = dados['idArea']
                assunto = dados['assunto']
                dataAula = dados['dataAula']
                horario = dados['horario']
                dt = converter_para_datetime(data=dataAula, horario=horario)
                Aula(idProfessor=Professor.objects.get(user=request.user), idArea=idArea, assunto=assunto, datetime=dt).save()
                return redirect('aula:index_aula', request.user.username)
            else:
                pass
                #message
        else:
            form_aula = AulaForm()
        context = {
            'username': username,
            'form_aula': form_aula,
            'full_name': request.user.get_full_name(),
            'areas': Area.objects.all()
        }
        return render(request, 'aula/add_aula.html', context)

    def get_aula(request, username, id):
        aula = Aula.objects.get(pk=id)
        context = {
            'username': username,
            'full_name': request.user.get_full_name(),
            'aula': aula
        }
        return render(request, 'aula/get_aula.html', context)
