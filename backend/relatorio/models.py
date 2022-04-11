from django.db import models
from users.models import Professor, Administrador
from aula.models import Area, Aula

# Create your models here.
class Avaliacao(models.Model):
    idAula = models.ForeignKey(Aula, on_delete=models.CASCADE, on_update=models.CASCADE, null=False)
    idAluno = models.ForeignKey(Professor, on_delete=models.CASCADE, on_update=models.CASCADE, null=False)

class Relatorio(models.Model):
    idAdmin = models.ForeignKey(Administrador, on_delete=models.CASCADE, on_update=models.CASCADE, null=False)
    idAvaliacao = models.ForeignKey(Avaliacao, on_delete=models.CASCADE, on_update=models.CASCADE, null=False)
    idArea = models.ForeignKey(Area, on_delete=models.CASCADE, on_update=models.CASCADE, null=False)
