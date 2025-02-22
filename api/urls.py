from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import register_user, logout_user, AlbumViewSet, SongViewSet, PlaylistViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

# Konfigurasi Schema Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="OpenMusic API",
        default_version="v1",
        description="Dokumentasi OpenMusic API menggunakan Django REST Framework",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="admin@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)

router = DefaultRouter()
router.register(r'albums', AlbumViewSet, basename="album")
router.register(r'songs', SongViewSet, basename="song")
router.register(r'playlists', PlaylistViewSet, basename="playlist")

urlpatterns = [
    path('auth/register/', register_user, name="register"),
    path('auth/login/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('auth/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('auth/logout/', logout_user, name="logout"),
    path('', include(router.urls)),

    # Swagger & ReDoc URLs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc-ui'),
    path('swagger.json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger.yaml/', schema_view.without_ui(cache_timeout=0), name='schema-yaml'),
]
