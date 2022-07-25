from aula import views, views_aula_do_aluno
from django.urls import path

app_name = 'aula'
urlpatterns = [
    # /aulas/
    path("prof/<username>", views.AulaTemplate.index_aula_prof, name='index_aula_prof'),
    path("list", views.AulaTemplate.index_aula_admin, name='index_aula_admin'),
    path("add", views.AulaTemplate.adicionar_aula, name='adicionar_aula'),
    path("add/recorrentes/<int:turma_id>", views.AulaTemplate.adicionar_aulas_recorrentes, name='adicionar_aulas_recorrentes'),
    path("edit/<int:id>", views.AulaTemplate.editar_aula, name='editar_aula'),
    path("delete/<int:id>", views.AulaTemplate.deletar_aula_template, name='deletar_aula_template'),
    path("delete/<int:id>/confirm", views.AulaTemplate.deletar_aula, name='deletar_aula'),
    path("detail/<int:id>", views.AulaTemplate.detalhar_aula, name='detalhar_aula'),

    # aula do aluno
    path("<int:matr>/detail", views_aula_do_aluno.AulaDoAlunoView.aulas_do_aluno, name='aulas_do_aluno'),
    path("detail/<int:aula_id>/aluno", views_aula_do_aluno.AulaDoAlunoView.add_aluno_em_aula, name='add_aluno_em_aula'),
    path("detail/<int:aula_id>/aluno/delete/<int:aluno_id>", views_aula_do_aluno.AulaDoAlunoView.remover_aluno_de_aula_template, name='remover_aluno_de_aula_template'),
    path("detail/<int:aula_id>/aluno/delete/<int:aluno_id>/confirm", views_aula_do_aluno.AulaDoAlunoView.remover_aluno_de_aula, name='remover_aluno_de_aula'),
]
