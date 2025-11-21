from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('reports/', views.get_all_reports, name='report-list'),
]

# Append media URL patterns (if needed)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
