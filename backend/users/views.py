from django.shortcuts import redirect, render
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
from users.utils import is_admin
from .controller import add_admin_controller, add_prof_controller
from .forms import AdministradorForm, ProfessorForm, UserForm

@permission_required('users.add_administrador', login_url='/', raise_exception=True)
def add_admin_template(request):
    if request.method == 'POST':
        form_user = UserForm(request.POST)
        form_admin = AdministradorForm(request.POST)
        created = add_admin_controller(form_user=form_user, form_admin=form_admin)
        if created:
            messages.success(request, "Administrador(a) criado com sucesso!")
            return redirect('login:index')
        else:
            messages.error(request, "Erro ao criar administrador(a)! Provavelmente já existe um usuário com esse username ou siape.")
    else:
        form_user = UserForm()
        form_admin = AdministradorForm()

    context = {
        'form_admin': form_admin,
        'form_user': form_user
    }
    context.update(is_admin(request))
    return render(request, 'users/add_admin_template.html', context)

@permission_required('users.add_professor', login_url='/', raise_exception=True)
def add_prof_template(request):
    if request.method == 'POST':
        form_user = UserForm(request.POST)
        form_prof = ProfessorForm(request.POST)
        created = add_prof_controller(form_user=form_user, form_prof=form_prof)
        if created:
            messages.success(request, "Professor(a) criado com sucesso!")
            return redirect('login:index')
        else:
            messages.error(request, "Erro ao criar professor(a)! Provavelmente já existe um usuário com esse username ou siape.")
    else:
        form_user = UserForm()
        form_prof = ProfessorForm()
    context = is_admin(request)
    return render(request, 'users/add_prof_template.html', context)
