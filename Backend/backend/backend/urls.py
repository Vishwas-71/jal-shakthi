from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from reports.views import ReportViewSet

router = DefaultRouter()
router.register(r'reports', ReportViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include('reports.urls')),
]



    