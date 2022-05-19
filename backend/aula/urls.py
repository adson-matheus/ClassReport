from aula import views
from django.urls import path

app_name = 'aula'
urlpatterns = [
    # /aula/
    path("list", views.AulaTemplate.index_aula_admin, name='index_aula_admin'),
    path("prof/<username>", views.AulaTemplate.index_aula, name='index_aula'),
    path("add", views.AulaTemplate.add_aula, name='add_aula'),
    path("detail/<int:id>", views.AulaTemplate.get_aula, name='get_aula'),
    path("prof/<username>/edit/<int:id>", views.AulaTemplate.edit_aula, name='edit_aula'),
    path("delete/<int:id>", views.AulaTemplate.delete_aula_template, name='delete_aula_template'),
    path("delete/<int:id>/confirm", views.AulaTemplate.delete_aula, name='delete_aula'),
]
