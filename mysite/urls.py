from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls')),
]

if settings.DEBUG:      # т.е. если DEBUG = True
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)