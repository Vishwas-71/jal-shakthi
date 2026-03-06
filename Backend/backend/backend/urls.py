from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from reports.views import ReportViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'reports', ReportViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include(router.urls)),
    path('api/', include('reports.urls')),

    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]

# 🔥 THIS PART SERVES IMAGES
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)