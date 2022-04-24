from django.shortcuts import redirect, render
from django.contrib.auth.models import User, Group
from .models import Area, Administrador, Professor
from .forms import AdministradorForm, ProfessorForm, UserForm
from .serializers import AreaSerializer
from rest_framework import generics, permissions

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
