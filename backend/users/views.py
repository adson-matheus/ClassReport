from django.http import HttpResponse
from django.shortcuts import render
from .models import Administrador
from django.contrib.auth.models import UserManager

# Create your views here.
def index(request):
    return HttpResponse("hello, world")

def add_admin_template(request):
    return render(request, 'users/add_admin_template.html')

