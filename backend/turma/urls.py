from turma import views
from django.urls import path

app_name = 'turma'
urlpatterns = [
    path('list', views.listar_turmas, name='listar_turmas'),
]
