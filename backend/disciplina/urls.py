from disciplina import views
from django.urls import path

app_name = 'disciplina'

urlpatterns = [
    path('list', views.listar_disciplinas, name='listar_disciplinas'),
    path('add', views.add_disciplina, name='add_disciplina'),
]