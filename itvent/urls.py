from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from events import views
from homepage import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('events/', include('events.urls')),
    path('learn/', include('learn.urls')),
    path('aboutus/', include('homepage.urls')),
    path('auth/', include('auth_app.urls')),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
