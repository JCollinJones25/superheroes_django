from django.db import models

# Create your models here.

class Hero(models.Model):

    name = models.CharField(max_length=100)
    secret_identity = models.CharField(max_length=100)
    img = models.CharField(max_length=500)
    bio = models.TextField(max_length=500)
    powers = models.CharField(max_length=200)
    universe = models.CharField(max_length=50)
    affiliations = models.TextField(max_length=500)
    villains = models.TextField(max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Villain(models.Model):

    name = models.CharField(max_length=150)
    img = models.CharField(max_length=500)
    bio = models.TextField(max_length=500)
    powers = models.CharField(max_length=200)
    universe = models.CharField(max_length=50)
    affiliations = models.TextField(max_length=500)
    nemesis = models.ForeignKey(Hero, on_delete=models.CASCADE, related_name='enemies')

    def __str__(self):
        return self.name

    class Meta: 
        ordering = ['name']

class Comic(models.Model):

    title = models.CharField(max_length=100)
    img = models.CharField(max_length=500, default='https://cdn.europosters.eu/image/1300/posters/dc-comics-rebirth-i80856.jpg')
    author = models.TextField(max_length=100, default='not entered')
    year = models.CharField(max_length=20, default='TBD') 
    heroes = models.ManyToManyField(Hero)
    villains = models.ManyToManyField(Villain)

    def __str__(self):
        return self.title
