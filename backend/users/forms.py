from django import forms

from .models import Administrador, Professor

class AddAdministradorForm(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = ['siape', 'first_name', 'last_name', 'username', 'email', 'password']

class AddProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['siape', 'idArea', 'first_name', 'last_name', 'username', 'email', 'password']
