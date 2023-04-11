from django.contrib import admin
from django.urls import path, include
from events import views
from homepage import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('events/', include('events.urls')),
    path('learn/', include('learn.urls'))
]
