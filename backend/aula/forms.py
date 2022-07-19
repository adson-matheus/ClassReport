from django.forms import IntegerField, ModelForm, Form, MultipleChoiceField, DateField, DateInput, TimeField
from .models import Aula
from users.models import Aluno

alunos = Aluno.objects.all()
CHOICES = ( (aluno.id, aluno.nome) for aluno in alunos)

class AulaForm(ModelForm):
    class Meta:
        model = Aula
        fields = '__all__'

class AulaFormEdit(ModelForm):
    class Meta:
        model = Aula
        fields = '__all__'

class AulaDoAlunoForm(Form):
    alunos = MultipleChoiceField(choices=CHOICES, required=True)

class AulasRecorrentesForm(ModelForm):
    data_inicio = DateField(required=True, label='Data de início', widget=DateInput(attrs={'type': 'date'}))
    data_fim = DateField(required=True, label='Data de fim', widget=DateInput(attrs={'type': 'date'}))
    intervalo = IntegerField(required=True, label='Intervalo de dias', initial=7)
    hora = TimeField(required=True, label='Hora', widget=DateInput(attrs={'type': 'time'}))
    alunos = MultipleChoiceField(choices=CHOICES, required=False)

    class Meta:
        model = Aula
        exclude = ['datetime']
