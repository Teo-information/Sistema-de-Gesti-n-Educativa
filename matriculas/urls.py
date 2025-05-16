from django.urls import path
from . import views

app_name = 'matriculas'

urlpatterns = [
    path('', views.matricula_list, name='list'),
    path('crear/', views.matricula_create, name='create'),
    path('<int:pk>/', views.matricula_detail, name='detail'),
    path('<int:pk>/editar/', views.matricula_update, name='update'),
    path('<int:pk>/eliminar/', views.matricula_delete, name='delete'),
] 