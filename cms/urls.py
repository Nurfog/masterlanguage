from django.urls import path
from . import views

urlpatterns = [
    path('crear_pais/', views.crear_pais, name='crear_pais'),
    path('lista_paises/', views.lista_paises, name='lista_paises'),
    path('editar_pais/<int:id>/', views.editar_pais, name='editar_pais'),
    path('eliminar_pais/<int:id>/', views.eliminar_pais, name='eliminar_pais'),
    path('crear_region/', views.crear_region, name='crear_region'),
    path('lista_region/', views.lista_region, name='lista_region'),
    path('editar_region/<int:id>/', views.editar_region, name='editar_region'),
    path('eliminar_region/<int:id>/', views.eliminar_region, name='eliminar_region'),
    path('crear_provincia/', views.crear_provincia, name='crear_provincia'),
    path('lista_provincia/', views.lista_provincia, name='lista_provincia'),
    path('editar_provincia/<int:id>/', views.editar_provincia, name='editar_provincia'),
    path('eliminar_provincia/<int:id>/', views.eliminar_provincia, name='eliminar_provincia'),
    path('crear_comuna/', views.crear_comuna, name='crear_comuna'),
    path('lista_comuna/', views.lista_comunas, name='lista_comuna'),
    path('editar_comuna/<int:id>/', views.editar_comuna, name='editar_comuna'),
    path('eliminar_comuna/<int:id>/', views.eliminar_comuna, name='eliminar_comuna'),
]