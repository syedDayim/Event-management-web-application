from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('changepassword/', views.user_change_password, name='changepassword'),

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='auth_app/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='auth_app/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', views.PasswordResetConfirmViewCustom.as_view(template_name='auth_app/password_reset_confirm.html'), name='password_reset_confirm'),

    path('password-reset/complete/', auth_views.PasswordResetView.as_view(template_name='auth_app/password_reset_complete.html'), name='password_reset_complete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
