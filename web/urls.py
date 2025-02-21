from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [    
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('courses/', views.courses, name='courses'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('error_404/', views.error_404, name='error_404'),
    path('account/', views.login, name='account'),    
]

