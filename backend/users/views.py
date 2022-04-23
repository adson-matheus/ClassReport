from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import Area, Administrador, Professor
from .forms import AdministradorForm, ProfessorForm, UserForm
from .serializers import AreaSerializer
from rest_framework import generics

def add_admin_controlador(form_user, form_admin):
    '''
        Cria administrador adicionando o respectivo siape.
    '''
    if form_user.is_valid() and form_admin.is_valid():
        get_siape = form_admin.cleaned_data['siape']
        user = add_user_generico(form_user=form_user)
        Administrador(user=user, siape=get_siape).save()
        return True

def add_admin_template(request):
    if request.method == 'POST':
        form_user = UserForm(request.POST)
        form_admin = AdministradorForm(request.POST)
        criou = add_admin_controlador(form_user=form_user, form_admin=form_admin)
        if criou:
            return redirect('login:index')
    else:
        form_user = UserForm()
        form_admin = AdministradorForm()

    context = {
        'form_admin': form_admin,
        'form_user': form_user
    }
    return render(request, 'users/add_admin_template.html', context)

def add_prof_controlador(form_user, form_prof):
    '''
        Cria professor adicionando o respectivo siape e id da Area que atua.
    '''
    if form_user.is_valid() and form_prof.is_valid():
        get_siape = form_prof.cleaned_data['siape']
        get_area = form_prof.cleaned_data['idArea']
        user = add_user_generico(form_user=form_user)
        Professor(user=user, siape=get_siape, idArea=get_area).save()
        return True

def add_prof_template(request):
    areas = Area.objects.all()
    if request.method == 'POST':
        form_user = UserForm(request.POST)
        form_prof = ProfessorForm(request.POST)
        criou = add_prof_controlador(form_user=form_user, form_prof=form_prof)
        if criou:
            return redirect('login:index')
        form = ProfessorForm(request.POST)
    else:
        form = ProfessorForm()

    context = {
        'form': form,
        'areas': areas
    }
    return render(request, 'users/add_prof_template.html', context)

def add_user_generico(form_user):
    '''
        Cria, salva e retorna um User.
    '''
    user = User.objects.create_user(
        username = form_user.cleaned_data['username'],
        password = form_user.cleaned_data['password'],
        email = form_user.cleaned_data['email'],
        first_name = form_user.cleaned_data['first_name'],
        last_name = form_user.cleaned_data['last_name'],
    )
    return user

class ListarAreas(generics.ListCreateAPIView):
    """
        View que retorna a API responsável por criar e listar as áreas
    """
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

class DetalhesAreas(generics.RetrieveUpdateDestroyAPIView):
    """
        View que retorna a API responsável por atualizar e deletar as áreas
    """
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
