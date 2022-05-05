from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm, TimeField, DateField
from .models import Aula

class AulaForm(ModelForm):
    dataAula = DateField(required=True, label='Data da aula')
    horario = TimeField(required=True, label='Horário da aula')
    class Meta:
        model = Aula
        exclude = ['idProfessor', 'datetime']

class AulaFormEdit(ModelForm):
    dataAula = DateField(required=True, label='Data da aula', initial=Aula.datetime)
    horario = TimeField(required=True, label='Horário da aula')
    class Meta:
        model = Aula
        exclude = ['idProfessor',]
