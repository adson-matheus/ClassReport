from aula import views
from django.urls import path

app_name = 'aula'
urlpatterns = [
    # /aulas/
    path("prof/<username>", views.AulaTemplate.index_aula_prof, name='index_aula_prof'),
    path("list", views.AulaTemplate.index_aula_admin, name='index_aula_admin'),
    path("add", views.AulaTemplate.add_aula, name='add_aula'),
    path("edit/<int:id>", views.AulaTemplate.edit_aula, name='edit_aula'),
    path("delete/<int:id>", views.AulaTemplate.delete_aula_template, name='delete_aula_template'),
    path("delete/<int:id>/confirm", views.AulaTemplate.delete_aula, name='delete_aula'),
    path("detail/<int:id>", views.AulaTemplate.get_aula, name='get_aula'),

    # aula do aluno
    path("detail/<int:id_aula>/aluno", views.AulaDoAlunoView.index_alunos, name='index_alunos'),
    #path("detail/<int:id_aula>/aluno/add", views.AulaDoAlunoView.add_aluno_em_aula, name='add_aluno_em_aula'),
]
