from django.forms import ModelForm, TimeField, DateField
from .models import Aula

class AulaForm(ModelForm):
    class Meta:
        model = Aula
        fields = '__all__'

class AulaFormEdit(ModelForm):
    class Meta:
        model = Aula
        fields = '__all__'
