from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    prof      = models.ForeignKey(User, on_delete=models.CASCADE)
    name      = models.CharField(max_length=100)
    title     = models.CharField(max_length=200)
    content   = models.TextField()
    slug      = models.SlugField(blank=True, null=True)
    likes     = models.ManyToManyField(User, related_name='likes',blank=True)
    fav       = models.ManyToManyField(User, related_name='fav', blank=True)


    def __str__(self):
        return self.name



class Comments(models.Model):
    profile = models.ForeignKey(Profile, related_name='comments', on_delete=models.CASCADE)
    name    = models.CharField(max_length=200)
    email   = models.EmailField()
    body    = models.TextField()



    def __str__(self):
        return self.name

