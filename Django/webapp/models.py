from django.db import models
import graphene

TYPE_CHOICES = (
    ('band' , 'Band'),
    ('Solo' , 'Solo'),

)
#Song table
class Song(models.Model):
    Name = models.CharField(max_length=50)
    Genre = models.CharField(max_length=10)
    Artist = models.CharField(max_length=15)
    Album = models.CharField(max_length=50)

    def __str__(self):
        return self.Name
#Album table
class Album(models.Model):
    Name = models.CharField(max_length=50)
    Genre = models.CharField(max_length=10)
    Artist = models.TextField(max_length=500)
    Song = models.TextField(max_length=500)
    DatePublihsed = models.DateField()

    def __str__(self):
        return self.Name
#Artist table
class Artist(models.Model):
    Name = models.CharField(max_length=50)
    Form = models.CharField(max_length=10 , choices=TYPE_CHOICES , default='band')
    Album = models.TextField(max_length=500)
    Song = models.TextField(max_length=500)
    PreferredGenre = models.CharField(max_length=15)
    DateOfFormationorBirth= models.DateField()
    Bio = models.TextField(max_length=500)

    def __str__(self):
        return self.Name