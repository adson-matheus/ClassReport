from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def index(request):
    group = Group.objects.get(name='grp_administradores')
    if group in request.user.groups.all():
        #return render
        return HttpResponse('adm')
    else:
        #return render
        return HttpResponse('prof')


def login_usuario(request):
    if request.method == "POST":
        user = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=user, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('login:index')
        else:
            return redirect('login:login_usuario')

    return render(request, 'login/login.html')
