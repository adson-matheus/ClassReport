from users import views
from django.urls import path

app_name = 'users'
urlpatterns = [
    path('admin/add', views.add_admin_template, name='add_admin_template'),
    path('alunos', views.AlunoTemplate.index_aluno, name='index_aluno'),
    path('alunos/add', views.AlunoTemplate.add_aluno, name='add_aluno'),
    path('alunos/edit/<int:matr>', views.AlunoTemplate.edit_aluno, name='edit_aluno'),
    path('alunos/delete/<int:matr>', views.AlunoTemplate.delete_aluno_template, name='delete_aluno_template'),
    path('alunos/delete/<int:matr>/confirm', views.AlunoTemplate.delete_aluno, name='delete_aluno'),
    path('prof', views.ProfessorTemplate.index_professor, name='index_prof'),
    path('prof/add', views.add_prof_template, name='add_prof_template'),
    path('prof/edit/<int:siape>', views.ProfessorTemplate.edit_professor, name='edit_professor'),
    path('prof/delete/<int:siape>', views.ProfessorTemplate.delete_professor_template, name='delete_prof_template'),
    path('prof/delete/<int:siape>/confirm', views.ProfessorTemplate.delete_professor, name='delete_prof'),
]
