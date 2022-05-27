from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, permission_required
from users.utils import is_admin
from django.contrib.auth.models import User, Group
from disciplina.models import Disciplina
from .models import Administrador, Professor, Aluno
from .forms import AdministradorForm, ProfessorForm, UserForm, AlunoForm, EditarAlunoForm
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
    context.update(is_admin(request))
    return render(request, 'users/add_admin_template.html', context)

def add_prof_controller(form_user, form_prof):
    '''
        Cria professor adicionando o respectivo siape.
    '''
    if form_user.is_valid() and form_prof.is_valid():
        get_siape = form_prof.cleaned_data['siape']
        user = add_generic_user(form_user=form_user, group_name='grp_professores')
        Professor(user=user, siape=get_siape).save()
        return True

def add_prof_template(request):
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
    }
    context.update(is_admin(request))
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

class AlunoTemplate:
    """
        Aluno possui matrícula e nome. Aluno assiste 'n' aulas.
        Aluno NÃO possui acesso ao sistema.
    """
    @permission_required('users.view_aluno', login_url='/', raise_exception=True)
    def index_aluno(request):
        alunos = Aluno.objects.all()
        context = {
            'alunos': alunos,
            'full_name': request.user.get_full_name()
        }
        context.update(is_admin(request))
        return render(request, 'users/aluno/alunos.html', context)

    @permission_required('users.add_aluno', login_url='/', raise_exception=True)
    def add_aluno(request):
        """
            Administrador adiciona aluno
        """
        if request.method == 'POST':
            form = AlunoForm(request.POST)
            if form.is_valid():
                form.save()
                # msg
                return redirect('users:index_aluno')
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
        context.update(is_admin(request))
        return render(request, 'users/aluno/add_aluno.html', context)

    @permission_required('users.change_aluno', login_url='/', raise_exception=True)
    def edit_aluno(request, matr):
        aluno = Aluno.objects.get(matricula=matr)
        if request.method == 'POST':
            form = EditarAlunoForm(request.POST, instance=aluno)
            if form.is_valid():
                # msg
                form.save()
                return redirect('users:index_aluno')
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
        context.update(is_admin(request))
        return render(request, 'users/aluno/edit_aluno.html', context)

    @permission_required('users.delete_aluno', login_url='/', raise_exception=True)
    def delete_aluno_template(request, matr):
        aluno = Aluno.objects.get(matricula=matr)
        context = {
            'full_name': request.user.get_full_name(),
            'aluno': aluno,
        }
        context.update(is_admin(request))
        return render(request, 'users/aluno/delete_aluno.html', context)

    @permission_required('users.delete_aluno', login_url='/', raise_exception=True)
    def delete_aluno(request, matr):
        aluno = Aluno.objects.get(matricula=matr)
        aluno.delete()
        # msg
        return redirect('users:index_aluno')

@login_required
class ProfessorTemplate:
    """
        CRUD de Professor
    """
    def index_professor(request):
        context = {
            'professores': Professor.objects.exclude(user__is_active=False),
            'full_name': request.user.get_full_name(),
            'is_admin': True,
        }
        return render(request, 'users/prof/professores.html', context)

    def delete_professor_template(request, siape):
        professor = Professor.objects.get(siape=siape)
        disciplinas = Disciplina.objects.filter(idProfessor=professor.siape)
        context = {
            'full_name': request.user.get_full_name(),
            'professor': professor,
            'disciplinas': disciplinas,
        }
        context.update(is_admin(request))
        return render(request, 'users/prof/delete_prof.html', context)

    def delete_professor(request, siape):
        professor = Professor.objects.get(siape=siape)
        professor.user.is_active = False
        #professor.delete()
        # msg
        return redirect('users:index_prof')
