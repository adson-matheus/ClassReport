from login import views
from django.urls import path

app_name = 'login'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_usuario, name='login_usuario'),
    path('logout/', views.logout_usuario, name='logout_usuario'),
]