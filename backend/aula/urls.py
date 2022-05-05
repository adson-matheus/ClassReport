from aula import views
from django.urls import path

app_name = 'aula'
urlpatterns = [
    path("prof/<username>", views.AulaTemplate.index_aula, name='index_aula'),
    path("prof/<username>/add", views.AulaTemplate.add_aula, name='add_aula'),
    path("prof/<username>/detail/<int:id>", views.AulaTemplate.get_aula, name='get_aula'),
    path("prof/<username>/edit/<int:id>", views.AulaTemplate.edit_aula, name='edit_aula'),
]
