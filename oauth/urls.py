from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path ('account/', include('django.contrib.auth.urls')),
    path('account/signup/', views.register_page, name='register'),
    path ('account/logout/', views.logout_page, name='logout'),
    path('accounts/', include('allauth.urls')),
    
]