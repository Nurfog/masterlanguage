from django.urls import path
from . import views

urlpatterns = [
    path('account/login/', views.login_page, name='cuentas'),
    path('account/logout/', views.logout_page, name='logout'),
    path('account/register/', views.register_page, name='register'),
    path('account/profile/', views.profile_page, name='profile'),
    path('account/profile/edit/', views.edit_profile, name='edit_profile'),
    path('account/password_change/', views.change_password, name='change_password'),
    path('account/password_reset/', views.password_reset_request, name='password_reset'),
    path('account/password_reset/done/', views.password_reset_done, name='password_reset_done'),
    path('account/reset/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    path('account/reset/done/', views.password_reset_complete, name='password_reset_complete'),
    path('account/activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('account/activate/success/', views.activate_success, name='activate_success'),
    path('account/activate/failed/', views.activate_failed, name='activate_failed'),
    path('account/activate/resend/', views.resend_activation_email, name='resend_activation_email'),    
]