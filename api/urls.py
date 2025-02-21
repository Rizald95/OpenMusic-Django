from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import register_user, logout_user, AlbumViewSet, SongViewSet, PlaylistViewSet

router = DefaultRouter()
router.register(r'albums', AlbumViewSet)
router.register(r'songs', SongViewSet)
router.register(r'playlists', PlaylistViewSet)

urlpatterns = [
    path('auth/register/', register_user, name="register"),
    path('auth/login/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('auth/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('auth/logout/', logout_user, name="logout"),
    path('', include(router.urls)),
]
