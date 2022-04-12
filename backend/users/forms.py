from django import forms

from .models import Administrador

class AddAdministradorForm(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = ['siape', 'first_name', 'last_name', 'username', 'email', 'password']
