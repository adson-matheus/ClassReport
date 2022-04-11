from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Area(models.Model):
    nome = models.CharField(verbose_name='nome', primary_key=False, max_length=100, null=False)
    
    class Meta:
        ordering = ('-id',)
    def __str__(self):
        return self.nome

class Administrador(User):
    siape = models.CharField(verbose_name='siape', primary_key=True, max_length=20, null=False)

    # def add_administrador(siape, nome, email, password):
    #     user = User.objects.create_user(nome, email, password)
    #     user.siape = siape
    #     user.save()


    class Meta:
        ordering = ('first_name',)
    def __str__(self):
        return User.get_full_name(self)

class Aluno(models.Model):
    matricula = models.CharField(verbose_name='matricula', primary_key=True, max_length=20, null=False)
    nome = models.CharField(verbose_name='nome', primary_key=False, max_length=100, null=False)

    class Meta:
        ordering = ('-nome',)
    def __str__(self):
        return self.nome

class Professor(User):
    siape = models.CharField(verbose_name='siape', primary_key=True, max_length=20, null=False)
    idArea = models.ForeignKey(Area, on_delete=models.CASCADE, null=False)

    class Meta:
        ordering = ('first_name',)
    def __str__(self):
        return User.get_full_name(self)
