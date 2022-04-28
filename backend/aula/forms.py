from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm, Textarea, TimeField, DateField
from .models import Aula

class AulaForm(ModelForm):
    dataAula = DateField(required=True, label='Data da aula')
    horario = TimeField(required=True, label='Horário da aula')
    class Meta:
        model = Aula
        exclude = ['idProfessor', 'datetime']
        widgets = {
            'assunto': Textarea(attrs={'cols': 50, 'rows': 15}),
        }
        # help_texts = {
        #     'assunto': _('O assunto/descrição da aula'),
        # }
        # error_messages = {
        #     'name': {
        #         'max_length': _("This writer's name is too long."),
        #     },
        # }
        # labels = {
        #     'assunto': _(''),
        # }
