from turma import views
from django.urls import path

app_name = 'turma'
urlpatterns = [
    path('list', views.listar_turmas, name='listar_turmas'),
    path('excluir/<int:id>', views.excluir_turma_template, name='excluir_turma_template'),
    path('excluir/<int:id>/confirmar', views.excluir_turma, name='excluir_turma'),
]
