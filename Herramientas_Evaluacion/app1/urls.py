from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crear/', views.crear_banda_con_perfil, name='crear_banda'),
    path('bandas/', views.listar_bandas, name='listar_bandas'),
    # path('bandas/editar/<int:id>/', views.editar_banda, name='editar_banda'),
    # path('bandas/eliminar/<int:id>/', views.eliminar_banda, name='eliminar_banda'),
]
