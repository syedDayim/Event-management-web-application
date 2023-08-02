from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.papers, name='papers'),
    path('user_papers/', views.user_papers, name='user_papers'),
]
