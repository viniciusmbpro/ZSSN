from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import SurvivorViewSet
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'survivors', SurvivorViewSet, basename='survivors')

urlpatterns = [
    path('interface/', include('interface.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)