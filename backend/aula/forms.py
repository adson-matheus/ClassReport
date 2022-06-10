from django.forms import ModelForm
from .models import Aula, AulaDoAluno

class AulaForm(ModelForm):
    class Meta:
        model = Aula
        fields = '__all__'

class AulaFormEdit(ModelForm):
    class Meta:
        model = Aula
        fields = '__all__'

# criar um form p/ pegar todos os ids marcados
# depois envia isso pra view
# da view faz um bulk create,
# usar js pra pegar todos os valores marcados
