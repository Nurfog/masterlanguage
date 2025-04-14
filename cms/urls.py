from django.urls import path
from . import views

urlpatterns = [
    path('crear_pais/', views.crear_pais, name='crear_pais'),
    path('lista_paises/', views.lista_paises, name='lista_paises'),\
]