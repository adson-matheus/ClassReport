from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.signals import user_logged_in, user_login_failed, user_logged_out
from .signals import *

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
            user_login_failed.connect(login_failed_message)
            return redirect('login:index')
    else:
        user_login_failed.connect(login_failed_message)

    return render(request, 'login/login.html')

def logout_usuario(request):
    user_logged_out.connect(logout_message)
    logout(request)
    return redirect('login:index')
