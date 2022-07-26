from turma import views
from django.urls import path

app_name = 'turma'
urlpatterns = [
    path('adicionar', views.adicionar_turma, name='adicionar_turma'),
    path('editar/<int:id>', views.editar_turma, name='editar_turma'),
    path('list', views.listar_turmas, name='listar_turmas'),
    path('list/<int:id>', views.listar_aulas_de_turma, name='listar_aulas_de_turma'),
    path('excluir/<int:id>', views.deletar_turma_template, name='deletar_turma_template'),
    path('excluir/<int:id>/confirmar', views.deletar_turma, name='deletar_turma'),
]
