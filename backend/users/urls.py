from users import views
from django.urls import path

app_name = 'users'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/admin/', views.add_admin_template, name='add_admin_template'),
]