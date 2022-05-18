from django import forms
from .models import Administrador, Professor, Aluno
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

class AdministradorForm(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = ['siape',]

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['siape',]

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'

class EditarAlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'
