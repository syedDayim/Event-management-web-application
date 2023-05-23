from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from events import views
from homepage import views

urlpatterns = [
    path('', views.aboutus, name='know more')
]
