from users import views
from django.urls import path

app_name = 'users'
urlpatterns = [
    path('add/admin/', views.add_admin_template, name='add_admin_template'),
    path('add/prof/', views.add_prof_template, name='add_prof_template'),
]