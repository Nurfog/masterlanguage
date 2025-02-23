from django.contrib import admin
from django.urls import path, include
from . import views
from allauth.account.views import LoginView

urlpatterns = [
    #path ('cuenta/', include('django.contrib.auth.urls')),
    #path('cuenta/register/', views.register_page, name='register'),
    #path ('cuenta/logout/', views.logout_page, name='logout'),
    path('accounts/', include('allauth.urls')),    
]