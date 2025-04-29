from django.urls import path
from . import views
urlpatterns = [
path('', views.lista_tarefas, name='lista_tarefas'),
path('deletar/<int:pk>/', views.deletar_tarefa, name='deletar_tarefa'),
path('atualizar/<int:pk>/', views.atualizar_tarefa, name='atualizar_tarefa'),
]