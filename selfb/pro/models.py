from django.db import models

# Create your models here.
class categories(models.Model):
    name = models.CharField(max_length=300)


class Blogpost(models.Model):
    blogid = models.IntegerField(default=0)
    topic = models.CharField(max_length=300)
    date = models.DateField()
    categories = models.CharField(max_length=300)
    author = models.CharField(max_length=100)
    bpost = models.TextField()
    bwholepost = models.TextField(default='description')
    tagline = models.TextField(default='tagline')

class comments(models.Model):
    coment = models.ForeignKey(Blogpost, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()


