from django.urls import path
from . import views

app_name = 'notas'

urlpatterns = [
    path('', views.nota_list, name='list'),
    path('crear/', views.nota_create, name='create'),
    path('<int:pk>/', views.nota_detail, name='detail'),
    path('<int:pk>/editar/', views.nota_update, name='update'),
    path('<int:pk>/eliminar/', views.nota_delete, name='delete'),
] 