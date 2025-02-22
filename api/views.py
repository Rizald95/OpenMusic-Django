from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, get_user_model  # Gunakan get_user_model()
from .models import Album, Song, Playlist
from .serializers import UserSerializer, AlbumSerializer, SongSerializer, PlaylistSerializer

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

User = get_user_model()  # Pastikan model user menggunakan model yang aktif

@swagger_auto_schema(
    method="post",
    request_body=UserSerializer,
    responses={201: openapi.Response("User successfully created", UserSerializer)},
)
@api_view(['POST'])
def register_user(request):
    """
    Mendaftarkan user baru.
    """
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_user(request):
    """
    Autentikasi user dan menghasilkan JWT token.
    """
    username = request.data.get("username")
    password = request.data.get("password")

    print(f"DEBUG: Mencari user {username}")  # Debugging

    user = get_user_model().objects.filter(username=username).first()
    if user:
        print(f"DEBUG: User ditemukan - {user.username}")
        print(f"DEBUG: Password cocok? {user.check_password(password)}")
    else:
        print("DEBUG: User tidak ditemukan")

    user = authenticate(username=username, password=password)

    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh)
        }, status=status.HTTP_200_OK)
    else:
        return Response({"detail": "No active account found with the given credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        
        
@api_view(['POST'])
def logout_user(request):
    """
    Logout user dengan menghapus token refresh dari sistem.
    """
    try:
        refresh_token = request.data.get("refresh")
        if refresh_token:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Refresh token is required"}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class AlbumViewSet(viewsets.ModelViewSet):
    """
    View untuk mengelola Album.
    """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [IsAuthenticated]


class SongViewSet(viewsets.ModelViewSet):
    """
    View untuk mengelola Lagu.
    """
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [IsAuthenticated]


class PlaylistViewSet(viewsets.ModelViewSet):
    """
    View untuk mengelola Playlist.
    """
    queryset = Playlist.objects.all()  # Menentukan queryset agar tidak ada error di router
    serializer_class = PlaylistSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Playlist.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
