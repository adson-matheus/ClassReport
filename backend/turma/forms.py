from django.forms import ModelForm
from .models import Turma

class TurmaForm(ModelForm):
    class Meta:
        model = Turma
        fields = '__all__'

class EditarTurmaForm(ModelForm):
    class Meta:
        model = Turma
        fields = '__all__'
