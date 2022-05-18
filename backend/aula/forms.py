from django.forms import ModelForm, TimeField, DateField
from .models import Aula

class AulaForm(ModelForm):
    class Meta:
        model = Aula
        fields = '__all__'

class AulaFormEdit(ModelForm):
    dataAula = DateField(required=True, label='Data da aula')
    horario = TimeField(required=True, label='Horário da aula')
    class Meta:
        model = Aula
        exclude = ['idProfessor', 'datetime',]
