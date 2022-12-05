from django.db import models

# Create your models here.
class Service(models.Model):
  name = models.TextField(max_length=200)
  description = models.TextField(max_length=400)
  img = models.TextField(max_length=100)
  action = models.TextField(max_length=100)

  def __str__(self):
    return self.name