from users import views, views_aluno, views_professor
from django.urls import path

app_name = 'users'
urlpatterns = [
    path('admin/add', views.adicionar_administrador, name='adicionar_administrador'),
    path('prof/add', views.adicionar_professor, name='adicionar_professor'),

    # alunos
    path('alunos', views_aluno.index_aluno, name='index_aluno'),
    path('alunos/add', views_aluno.adicionar_aluno, name='adicionar_aluno'),
    path('alunos/edit/<int:matr>', views_aluno.editar_aluno, name='editar_aluno'),
    path('alunos/delete/<int:matr>', views_aluno.deletar_aluno_template, name='deletar_aluno_template'),
    path('alunos/delete/<int:matr>/confirm', views_aluno.deletar_aluno, name='deletar_aluno'),

    # professores
    path('prof', views_professor.index_professor, name='index_prof'),
    path('prof/delete/<int:siape>', views_professor.deletar_professor_template, name='deletar_professor_template'),
    path('prof/delete/<int:siape>/confirm', views_professor.deletar_professor, name='deletar_professor'),
]
