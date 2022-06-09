from disciplina import views
from django.urls import path

app_name = 'disciplina'

urlpatterns = [
    path('listar', views.listar_disciplinas, name='listar_disciplinas'),
    path('add', views.add_disciplina, name='add_disciplina'),
    path('excluir/<int:id>', views.excluir_disciplina_template, name='excluir_disciplina_template'),
    path('excluir/<int:id>/confirmar', views.excluir_disciplina, name='excluir_disciplina'),
]
