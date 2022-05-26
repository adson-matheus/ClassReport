from users import views
from django.urls import path

app_name = 'users'
urlpatterns = [
    path('admin/add', views.add_admin_template, name='add_admin_template'),
    path('alunos', views.AlunoTemplate.index_aluno, name='index_aluno'),
    path('aluno/add', views.AlunoTemplate.add_aluno, name='add_aluno'),
    path('aluno/edit/<int:matr>', views.AlunoTemplate.edit_aluno, name='edit_aluno'),
    path('aluno/delete/<int:matr>', views.AlunoTemplate.delete_aluno_template, name='delete_aluno_template'),
    path('aluno/delete/<int:matr>/confirm', views.AlunoTemplate.delete_aluno, name='delete_aluno'),
    path('professores', views.ProfessorTemplate.index_professor, name='index_prof'),
    path('prof/add', views.add_prof_template, name='add_prof_template'),
    path('prof/delete/<int:siape>', views.ProfessorTemplate.delete_professor_template, name='delete_prof_template'),
    path('prof/delete/<int:siape>/confirm', views.ProfessorTemplate.delete_professor, name='delete_prof'),
]
