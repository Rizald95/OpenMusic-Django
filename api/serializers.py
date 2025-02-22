from rest_framework import serializers
from .models import User, Album, Song, Playlist

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)  # Pakai create_user()
        return user
        
class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'

class PlaylistSerializer(serializers.ModelSerializer):
    songs = serializers.PrimaryKeyRelatedField(
        queryset=Song.objects.all(),
        many=True,
        required=False  # Membuat field songs menjadi opsional
    )

    class Meta:
        model = Playlist
        fields = ['id', 'name', 'owner', 'songs']
        extra_kwargs = {'owner': {'read_only': True}}
