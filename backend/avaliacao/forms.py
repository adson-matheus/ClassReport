from django import forms
from .models import Avaliacao

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['checklist']

class EditarAvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['checklist']
