
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homeBuild.common.urls')),

    path('accounts/', include('homeBuild.accounts.urls')),
    path('projects/', include('homeBuild.projects.urls')),
    path('photos/', include('homeBuild.photos.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
