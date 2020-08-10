import graphene
from graphene_django.types import DjangoObjectType
from .models import Album
from .models import Artist
from .models import Song

class SongType(DjangoObjectType):
    class Meta:
        model= Song

class ArtistType(DjangoObjectType):
    class Meta:
        model= Artist

class AlbumType(DjangoObjectType):
    class Meta:
        model= Album

class Query(graphene.ObjectType):

    all_songs= graphene.List(SongType)
    all_artists = graphene.List(ArtistType)
    all_albums= graphene.List(AlbumType)

    def resolve_all_songs(self , info , **kwargs):

        return Song.objects.all()

    def resolve_all_artists(self, info, **kwargs):
        return Artist.objects.all()

    def resolve_all_albums(self, info, **kwargs):
        return Album.objects.all()