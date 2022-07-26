from .models import Administrador, Professor
from django.contrib.auth.models import User, Group

def add_admin_controller(form_user, form_admin):
    '''
        Cria administrador adicionando o respectivo siape.
    '''
    if form_user.is_valid() and form_admin.is_valid():
        get_siape = form_admin.cleaned_data['siape']
        user = add_generic_user(form_user=form_user, group_name='grp_administradores')
        Administrador(user=user, siape=get_siape).save()
        return True

def add_prof_controller(form_user, form_prof):
    '''
        Cria professor adicionando o respectivo siape.
    '''
    if form_user.is_valid() and form_prof.is_valid():
        get_siape = form_prof.cleaned_data['siape']
        user = add_generic_user(form_user=form_user, group_name='grp_professores')
        Professor(user=user, siape=get_siape).save()
        return True

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