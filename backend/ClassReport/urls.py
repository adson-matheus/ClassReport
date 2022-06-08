from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
    path('users/', include('users.urls')),
    path('aulas/', include('aula.urls')),
    path('disciplinas/', include('disciplina.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
