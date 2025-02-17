from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from homeBuild.photos import views

urlpatterns = [

    path('<int:pk>/', include([
        path('add/', views.PhotoAddPage.as_view(), name='photo-add'),
        # path('', views.PhotoDetailsPage.as_view(), name='photo-details'),
        # path('edit/', views.PhotoEditPage.as_view(), name='photo-edit'),
        # path('delete/', views.photo_delete_page, name='photo-delete'),
    ])),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)