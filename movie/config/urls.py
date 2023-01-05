from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

api_v1_patterns = [
    path("movies/", include("movies.api.v1.urls")),
    path("reviews/", include("reviews.api.v1.urls")),
]

api_patterns = [
    path("v1/", include(api_v1_patterns)),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(api_patterns)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
