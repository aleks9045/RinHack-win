from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app1.views import Files_ViewSet

router = routers.DefaultRouter()
router.register('files', Files_ViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("app1.urls")),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path('api/', include(router.urls))
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
