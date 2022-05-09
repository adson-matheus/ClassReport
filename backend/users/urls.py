from users import views
from django.urls import path

app_name = 'users'
urlpatterns = [
    path('prof/add/', views.add_prof_template, name='add_prof_template'),
    path('admin/add/', views.add_admin_template, name='add_admin_template'),
    path('admin/areas/', views.ListarAreas.as_view()),
    path('admin/areas/<int:pk>', views.DetalhesAreas.as_view()),
    path('aluno/add/', views.AlunoTemplate.add_aluno, name='add_aluno_template'),
]
