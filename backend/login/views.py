from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required()
def index(request):
    context = {
        'username': request.user.username,
        'full_name': request.user.get_full_name()
    }
    group = Group.objects.get(name='grp_administradores')
    if group in request.user.groups.all():
        context.update({'is_admin':True})
        return render(request, 'index/index_administrador.html', context)
    else:
        context.update({'is_admin':False})
        return render(request, 'index/index_professor.html', context)

def login_usuario(request):
    if request.method == "POST":
        user = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=user, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('login:index')
        else:
            messages.warning(request, 'Usuário ou Senha incorretos.')
            return redirect('login:login_usuario')

    return render(request, 'login/login.html')

def logout_usuario(request):
    logout(request)
    return redirect('login:index')