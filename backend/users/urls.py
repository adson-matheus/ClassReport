from users import views, views_aluno, views_professor
from django.urls import path

app_name = 'users'
urlpatterns = [
    path('admin/add', views.adicionar_administrador, name='adicionar_administrador'),
    path('prof/add', views.adicionar_professor, name='adicionar_professor'),

    # alunos
    path('alunos', views_aluno.index_aluno, name='index_aluno'),
    path('alunos/add', views_aluno.add_aluno, name='add_aluno'),
    path('alunos/edit/<int:matr>', views_aluno.edit_aluno, name='edit_aluno'),
    path('alunos/delete/<int:matr>', views_aluno.delete_aluno_template, name='delete_aluno_template'),
    path('alunos/delete/<int:matr>/confirm', views_aluno.delete_aluno, name='delete_aluno'),

    # professores
    path('prof', views_professor.index_professor, name='index_prof'),
    path('prof/delete/<int:siape>', views_professor.delete_professor_template, name='delete_prof_template'),
    path('prof/delete/<int:siape>/confirm', views_professor.delete_professor, name='delete_prof'),
]
