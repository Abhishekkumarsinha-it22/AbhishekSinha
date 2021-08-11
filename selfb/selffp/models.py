from django.db import models

class carrer1(models.Model):

    carname = models.CharField(max_length=20)
    rolname = models.CharField(max_length=300)
    dateoc = models.DateField()
    disc = models.TextField()

class testimonial(models.Model):
    Name = models.CharField(max_length=200)
    Profession = models.CharField(max_length=300)
    Company_name = models.CharField(max_length=300)
    feedback = models.TextField()


class education(models.Model):
    unname = models.CharField(max_length=200)
    degr = models.CharField(max_length=300)
    datep = models.DateField(null=True, blank=True)
    disc = models.TextField()

class certificate(models.Model):
    platform = models.CharField(max_length=200)
    course = models.CharField(max_length=300)
    dateofcompl = models.DateField()
    linkofcertificate = models.URLField()


class skills(models.Model):

    skillname = models.CharField(max_length=100)
    perc = models.CharField(max_length=300)

class abouts(models.Model):
    ab = models.TextField()
    finame = models.CharField(max_length=300)
    adfir = models.CharField(max_length=300)
    adsec = models.CharField(max_length=300)
    num = models.IntegerField()
    ema = models.EmailField()

