from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import Area, Administrador
from .forms import AdministradorForm, ProfessorForm, UserForm

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

def add_prof_template(request):
    areas = Area.objects.all()
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:index')
    else:
        form = ProfessorForm()
    return render(request, 'users/add_prof_template.html', {'form': form, 'areas': areas})
