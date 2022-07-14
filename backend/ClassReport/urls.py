from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
    path('users/', include('users.urls')),
    path('aulas/', include('aula.urls')),
    path('avaliacao/', include('avaliacao.urls')),
    path('disciplinas/', include('disciplina.urls')),
    path('turmas/', include('turma.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'), name='password_reset_complete'),
]
