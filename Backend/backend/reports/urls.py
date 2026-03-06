from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import register_user

urlpatterns = [

    # Register new user
    path('register/', register_user, name='register'),

]

# Serve media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)