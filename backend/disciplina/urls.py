from disciplina import views
from django.urls import path

app_name = 'disciplina'

urlpatterns = [
    path('listar', views.listar_disciplinas, name='listar_disciplinas'),
    path('add', views.adicionar_disciplina, name='adicionar_disciplina'),
    path('editar/<int:id>/', views.editar_disciplina, name='editar_disciplina'),
    path('excluir/<int:id>', views.deletar_disciplina_template, name='deletar_disciplina_template'),
    path('excluir/<int:id>/confirmar', views.excluir_disciplina, name='excluir_disciplina'),
]
