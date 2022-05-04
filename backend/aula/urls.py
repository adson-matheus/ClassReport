from aula import views
from django.urls import path

app_name = 'aulas'
urlpatterns = [
    path('prof/<username>', views.AulaTemplate.index, name='aulas'),
    path("prof/<username>/add", views.AulaTemplate.add_aula, name='add_aula'),
    path("prof/<username>/detail/<int:id>", views.AulaTemplate.get_aula, name='get_aula')
]
