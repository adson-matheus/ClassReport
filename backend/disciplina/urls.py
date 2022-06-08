from disciplina import views
from django.urls import path

app_name = 'disciplina'

urlpatterns = [
    path('list', views.listar_disciplinas, name='listar_disciplinas'),
]