from django.urls import path
from . import views
urlpatterns = [
    path('', views.events, name='events'),
    path('sucess/', views.registrationSuccess, name='sucess'),
]
