from django.urls import path
from . import views

urlpatterns = [
    path('accounts/login/', views.login_page, name='cuentas'),
    path('accounts/logout/', views.logout_page, name='logout'),
    path('accounts/register/', views.register_page, name='register'),
    path('accounts/profile/', views.profile_page, name='profile'),
    path('accounts/profile/edit/', views.edit_profile, name='edit_profile'),
    path('accounts/password_change/', views.change_password, name='change_password'),
    path('accounts/password_reset/', views.password_reset_request, name='password_reset'),
    path('accounts/password_reset/done/', views.password_reset_done, name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    path('accounts/reset/done/', views.password_reset_complete, name='password_reset_complete'),
    path('accounts/activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('accounts/activate/success/', views.activate_success, name='activate_success'),
    path('accounts/activate/failed/', views.activate_failed, name='activate_failed'),
    path('accounts/activate/resend/', views.resend_activation_email, name='resend_activation_email'),    
]