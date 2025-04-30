from django.urls import path
from . import views

urlpatterns = [
    path('account/ml/login/', views.login_page, name='cuentas'),
    path('account/ml/logout/', views.logout_page, name='logout'),
    path('account/ml/register/', views.register_page, name='register'),
    path('account/ml/profile/', views.profile_page, name='profile'),
    path('account/ml/profile/edit/', views.edit_profile, name='edit_profile'),
    path('account/ml/password_change/', views.change_password, name='change_password'),
]