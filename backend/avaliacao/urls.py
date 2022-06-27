from avaliacao import views
from django.urls import path

app_name = 'avaliacao'
urlpatterns = [
    # avaliacao
    path("<int:id_aula>/aluno/<int:id_aluno>", views.detalhar_avaliacao, name='detalhar_avaliacao'),
]
