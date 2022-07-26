from avaliacao import views
from django.urls import path

app_name = 'avaliacao'
urlpatterns = [
    # avaliacao
    path("<int:id_avaliacao>", views.detalhar_avaliacao, name='detalhar_avaliacao'),
    path("<int:id_avaliacao>/editar", views.editar_avaliacao, name='editar_avaliacao'),
    path("<int:aula_id>/aluno/<int:aluno_id>/add", views.adicionar_avaliacao, name='adicionar_avaliacao'),
    path("<int:id_avaliacao>/excluir", views.deletar_avaliacao_template, name='deletar_avaliacao_template'),
    path("<int:id_avaliacao>/excluir/confirmar", views.deletar_avaliacao, name='deletar_avaliacao'),
    path("<int:id_avaliacao>/pdf", views.exportar_pdf, name='exportar_pdf'),
]
