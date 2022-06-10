from django.db import models
from users.models import Professor

# Create your models here.
class Disciplina(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=255, null=True, blank=True)

    class Meta:
        ordering = ('-nome',)
    def __str__(self):
        return '{}'.format(self.nome)
