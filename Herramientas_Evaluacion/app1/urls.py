from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crear/', views.crear_banda_con_perfil, name='crear_banda'),
]
