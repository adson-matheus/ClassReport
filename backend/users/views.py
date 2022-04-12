from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import AddAdministradorForm
from django.contrib.auth.models import UserManager

# Create your views here.
def index(request):
    return HttpResponse("hello, world")

def add_admin_template(request):
    if request.method == 'POST':
        form = AddAdministradorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:index')
    else:
        form = AddAdministradorForm()
    return render(request, 'users/add_admin_template.html', {'form': form})
