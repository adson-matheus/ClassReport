from django.shortcuts import redirect, render
from .utils import converter_para_datetime
from users.models import Professor
from disciplina.models import Disciplina
from .forms import AulaForm, AulaFormEdit
from .models import Aula

class AulaTemplate:
    def index_aula(request, username):
        prof = Professor.objects.get(user=request.user)
        context = {
            'queryset': Aula.objects.filter(idProfessor = prof),
            'username': username,
            'full_name': request.user.get_full_name()
        }
        return render(request, 'aula/aulas.html', context)

    def index_aula_admin(request):
        context = {
            'aulas': Aula.objects.all(),
            'username': request.user.get_username(),
            'full_name': request.user.get_full_name()
        }
        return render(request, 'aula/index_aula_admin.html', context)

    def add_aula(request):
        if request.method == 'POST':
            form_aula = AulaForm(request.POST)
            if form_aula.is_valid():
                dados = form_aula.clean()
                assunto = dados['assunto']
                datetime = dados['datetime']
                disciplina = dados['disciplina']
                Aula(disciplina=disciplina, assunto=assunto, datetime=datetime).save()
                return redirect('aula:index_aula_admin')
            else:
                pass
                #message
        else:
            form_aula = AulaForm()
        context = {
            'form_aula': form_aula,
            'disciplinas': Disciplina.objects.all(),
            'full_name': request.user.get_full_name(),
        }
        return render(request, 'aula/add_aula.html', context)

    def get_aula(request, id):
        aula = Aula.objects.get(pk=id)
        context = {
            'full_name': request.user.get_full_name(),
            'aula': aula
        }
        return render(request, 'aula/get_aula.html', context)

    def edit_aula(request, username, id):
        aula = Aula.objects.get(pk=id)
        if request.method == 'POST':
            form_aula = AulaFormEdit(request.POST, instance=aula)
            if form_aula.is_valid():
                dados = form_aula.clean()
                dataAula = dados['dataAula']
                horario = dados['horario']

                dt = converter_para_datetime(data=dataAula, horario=horario)
                Aula(id=id,
                     idProfessor=Professor.objects.get(user=request.user),
                     assunto=dados['assunto'],
                     datetime=dt).save()
                # msg
                return redirect('aula:get_aula', request.user.username, id)
            else:
                # msg
                return redirect('aula:index_aula', request.user.username)
        else:
            form_aula = AulaFormEdit(instance=aula)
        context = {
            'form_aula': form_aula,
            'aula': aula,
            'full_name': request.user.get_full_name(),
            'username': username,
        }
        return render(request, 'aula/edit_aula.html', context)

    def delete_aula_template(request, id):
        aula = Aula.objects.get(pk=id)
        context = {
            'full_name': request.user.get_full_name(),
            'aula': aula,
        }
        return render(request, 'aula/delete_aula.html', context)

    def delete_aula(request, id):
        aula = Aula.objects.get(pk=id)
        aula.delete()
        return redirect('aula:index_aula_admin')
