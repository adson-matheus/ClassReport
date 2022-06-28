from avaliacao import views
from django.urls import path

app_name = 'avaliacao'
urlpatterns = [
    # avaliacao
    path("<int:id_aula>/aluno/<int:id_aluno>", views.detalhar_avaliacao, name='detalhar_avaliacao'),
    path("<int:id_avaliacao>/excluir", views.excluir_avaliacao_template, name='excluir_avaliacao_template'),
    path("<int:id_avaliacao>/excluir/confirmar", views.excluir_avaliacao, name='excluir_avaliacao'),
]
