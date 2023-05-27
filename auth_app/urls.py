from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('login/', views.login, name='login')
]
