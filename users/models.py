from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.base import Model
# Create your models here.

class CustomUserModel(AbstractUser):

  email = models.EmailField(unique=True)
  color = models.TextField(max_length=200, blank=True)
  image = models.URLField(blank=True)


  def __str__(self):
      return self.username
  

class Context(models.Model):
  name = models.TextField(max_length=100)
  description = models.TextField(max_length=300)
  creator = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)


  def __str__(self):
    return self.name  


class Notification(models.Model):

  host = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, blank=True, default=False)
  title = models.TextField(max_length=200)
  description = models.TextField(max_length=1000)
  link = models.URLField(blank=True)
  to = models.ManyToManyField(CustomUserModel, related_name="notifications", blank=True, default=False)
  createdAt = models.DateTimeField(auto_created=True, auto_now=True)
  context = models.ForeignKey(Context, on_delete=models.CASCADE)


  def __str__(self):
    return self.title

class TunnelEvent(models.Model):
  title = models.CharField(max_length=300)
  description = models.TextField()
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

class Tunnel(models.Model):
  title = models.CharField(max_length=300)
  description = models.TextField()
  user = models.ManyToManyField(CustomUserModel, related_name='tunnel')
  events = models.ManyToManyField(TunnelEvent, related_name='tunnel')
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)







