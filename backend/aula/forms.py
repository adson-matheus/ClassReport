from django.forms import ModelForm, Form, MultipleChoiceField
from .models import Aula, AulaDoAluno
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

