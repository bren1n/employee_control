from django.urls import path
from app import views

urlpatterns = [
    path('', views.hello_world),
    path('coordenador/', views.list_managers, name='list_managers'),
    path('coordenador/cadastrar/', views.create_manager, name='create_manager'),
    path('coordenador/editar/<int:pk>/', views.edit_manager, name='edit_manager'),
    path('coordenador/apagar/<int:pk>/', views.delete_manager, name='delete_manager'),
]
