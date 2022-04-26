from aula import views
from django.urls import path

app_name = 'aulas'
urlpatterns = [
    path('prof/<username>', views.crud_aula, name='aulas')
]
