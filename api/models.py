from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name="api_user_groups",  # Tambahkan related_name unik
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="api_user_permissions",  # Tambahkan related_name unik
        blank=True
    )
    
class Album(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField()

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    genre = models.CharField(max_length=100)
    performer = models.CharField(max_length=255)
    duration = models.IntegerField(null=True, blank=True)
    album = models.ForeignKey(Album, related_name='songs', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

class Playlist(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    songs = models.ManyToManyField(Song, related_name="playlists")

    def __str__(self):
        return self.name
