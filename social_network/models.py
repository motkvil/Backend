from django.db import models
from users.models import CustomUserModel

# Create your models here.
class SocialNetwork(models.Model):
  network = models.TextField(max_length=100)
  username = models.TextField(max_length=100)
  link = models.URLField()
  icon = models.URLField()

  def __str__(self):
    return self.username


class Unity(models.Model):
  name = models.CharField(max_length=300)
  description = models.CharField(max_length=400)
  titulo = models.CharField(max_length=300, null=True, blank=True)
  cuerpo = models.CharField(max_length=40000, null=True, blank=True)
  created = models.DateTimeField(auto_created=True, auto_now=True) 
  updated = models.DateTimeField(auto_created=True, auto_now=True)


class Universe(models.Model):
  name = models.CharField(max_length=200)
  description = models.CharField(max_length=400)
  titulo = models.CharField(max_length=300, null=True, blank=True)
  cuerpo = models.CharField(max_length=40000, null=True, blank=True)
  unities = models.ManyToManyField(Unity, related_name="universe")
  created = models.DateTimeField(auto_created=True, auto_now=True)
  updated = models.DateTimeField(auto_created=True, auto_now=True)

class Antimatter(models.Model):
  name = models.CharField(max_length=200)
  description = models.CharField(max_length=400)
  title = models.CharField(max_length=300, null=True, blank=True)
  cuerpo = models.CharField(max_length=40000, null=True, blank=True)
  dna = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, default=False)
  unity = models.ForeignKey(Unity, on_delete=models.CASCADE)
  universe = models.ForeignKey(Universe, on_delete=models.CASCADE)
  created = models.DateTimeField(auto_created=True, auto_now=True)
  updated = models.DateTimeField(auto_created=True, auto_now=True)
