from django.db import models
from django.utils import timezone
# Create your models here.


class Programok(models.Model):
    Title = models.CharField(max_length=256)
    ShortDescription = HTMLField(max_length=600)
    Date = models.DateTimeField()
    EventPic = models.ImageField(upload_to='programok')
    Location = models.CharField(max_length=256)
    Length = models.CharField(max_length=256)
    Category = models.CharField(max_length=256)
    Description = HTMLField(max_length=2000)


class Hirek(models.Model):
    Title = models.CharField(max_length=256)
    ShortDescription = HTMLField(max_length=600)
    Date = models.DateTimeField(default=timezone.now)
    NewsPic = models.ImageField(upload_to='hirek')
    Description = HTMLField(max_length=2000)


class Tamogatok(models.Model):
    SponsorPic = models.ImageField(upload_to='sponsors')


class Banner(models.Model):
    BannerPic = models.ImageField(upload_to='banner')
