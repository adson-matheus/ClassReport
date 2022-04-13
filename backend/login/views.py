from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return HttpResponse('pagina inicial')
    else:
        return redirect('login:login')

def login(request):
    return render(request, 'login/login.html')
