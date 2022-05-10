from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from .models import Area, Administrador, Professor, Aluno
from .forms import AdministradorForm, ProfessorForm, UserForm, AlunoForm, EditarAlunoForm
from .serializers import AreaSerializer
from rest_framework import generics, permissions
from django.http import HttpResponse

def add_admin_controller(form_user, form_admin):
    '''
        Cria administrador adicionando o respectivo siape.
    '''
    if form_user.is_valid() and form_admin.is_valid():
        get_siape = form_admin.cleaned_data['siape']
        user = add_generic_user(form_user=form_user, group_name='grp_administradores')
        Administrador(user=user, siape=get_siape).save()
        return True

def add_admin_template(request):
    if request.method == 'POST':
        form_user = UserForm(request.POST)
        form_admin = AdministradorForm(request.POST)
        created = add_admin_controller(form_user=form_user, form_admin=form_admin)
        if created:
            return redirect('login:index')
    else:
        form_user = UserForm()
        form_admin = AdministradorForm()

    context = {
        'form_admin': form_admin,
        'form_user': form_user
    }
    return render(request, 'users/add_admin_template.html', context)

def add_prof_controller(form_user, form_prof):
    '''
        Cria professor adicionando o respectivo siape e id da Area que atua.
    '''
    if form_user.is_valid() and form_prof.is_valid():
        get_siape = form_prof.cleaned_data['siape']
        get_area = form_prof.cleaned_data['idArea']
        user = add_generic_user(form_user=form_user, group_name='grp_professores')
        Professor(user=user, siape=get_siape, idArea=get_area).save()
        return True

def add_prof_template(request):
    areas = Area.objects.all()
    if request.method == 'POST':
        form_user = UserForm(request.POST)
        form_prof = ProfessorForm(request.POST)
        created = add_prof_controller(form_user=form_user, form_prof=form_prof)
        if created:
            return redirect('login:index')
        form = ProfessorForm(request.POST)
    else:
        form = ProfessorForm()

    context = {
        'form': form,
        'areas': areas
    }
    return render(request, 'users/add_prof_template.html', context)

def add_generic_user(form_user, group_name):
    '''
        Cria, salva e retorna um User; adiciona User ao seu grupo.
    '''
    user = User.objects.create_user(
        username = form_user.cleaned_data['username'],
        password = form_user.cleaned_data['password'],
        email = form_user.cleaned_data['email'],
        first_name = form_user.cleaned_data['first_name'],
        last_name = form_user.cleaned_data['last_name'],
    )
    get_group = Group.objects.get(name=group_name)
    get_group.user_set.add(user)
    return user

@login_required
class AlunoTemplate:
    """
        Aluno possui matrícula e nome. Aluno assiste 'n' aulas.
        Aluno NÃO possui acesso ao sistema.
    """
    def index_aluno(request):
        alunos = Aluno.objects.all()
        context = {
            'alunos': alunos,
            'full_name': request.user.get_full_name()
        }
        return render(request, 'users/alunos.html', context)

    def add_aluno(request):
        """
            Professor e Administrador adicionam aluno
        """
        if request.method == 'POST':
            form = AlunoForm(request.POST)
            if form.is_valid():
                form.save()
                # msg
                return redirect('login:index')
            else:
                return HttpResponse("Aluno já existe!")
                # msg
                pass
        else:
            form = AlunoForm()
        context = {
            'form': form,
            'user': request.user,
            'full_name': request.user.get_full_name()
        }
        return render(request, 'users/add_aluno_template.html', context)

    def edit_aluno(request, id):
        aluno = Aluno.objects.get(pk=id)
        if request.method == 'POST':
            form = EditarAlunoForm(request.POST, instance=aluno)
            if form.is_valid():
                # msg
                form.save()
                return redirect('login:index')
            else:
                # msg
                pass
        else:
            form = EditarAlunoForm(instance=aluno)
        context = {
            'aluno': aluno,
            'user': request.user,
            'full_name': request.user.get_full_name()
        }
        return render(request, 'users/editar_aluno_template.html', context)


class ListarAreas(generics.ListCreateAPIView):
    """
        View que retorna a API responsável por criar e listar as áreas
    """
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class DetalhesAreas(generics.RetrieveUpdateDestroyAPIView):
    """
        View que retorna a API responsável por buscar, atualizar e/ou deletar uma área
    """
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
