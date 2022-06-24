from turma import views
from django.urls import path

app_name = 'turma'
urlpatterns = [
    path('adicionar', views.adicionar_turma, name='adicionar_turma'),
    path('editar/<int:id>', views.editar_turma, name='editar_turma'),
    path('list', views.listar_turmas, name='listar_turmas'),
    path('list/<int:id>', views.listar_aulas_de_turma, name='listar_aulas_de_turma'),
    path('excluir/<int:id>', views.excluir_turma_template, name='excluir_turma_template'),
    path('excluir/<int:id>/confirmar', views.excluir_turma, name='excluir_turma'),
]
