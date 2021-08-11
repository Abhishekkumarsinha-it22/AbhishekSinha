from django.db import models


# Create your models here.
class Introduction(models.Model):
    head = models.CharField(max_length=100)
    disc = models.TextField()

class Fav(models.Model):
    recname = models.CharField(max_length=100)
    rectech = models.CharField(max_length=100)

class Projects(models.Model):

    aboutme = models.TextField(default='abhishek')
    topic = models.CharField(max_length=100)
    date = models.DateField()
    author = models.CharField(max_length=100)
    link = models.URLField()
    cont1 = models.TextField()
    cont2 = models.TextField()
    proid = models.IntegerField()
    categ = models.CharField(max_length=100)
    lang = models.CharField(max_length=100, default='python')

class comments(models.Model):
    coment = models.ForeignKey(Projects, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()










class categories(models.Model):
    name = models.CharField(max_length=300)

class HeadIntro(models.Model):
    topic = models.CharField(max_length=100)
    disc = models.TextField()

class Sharing(models.Model):
    disc = models.TextField()
    link = models.URLField()
    linkname = models.CharField(max_length=100, default='github')