from django.db import models

# Create your models here.
class Category(models.Model):
  title = models.TextField(max_length=1000)
  description = models.TextField(max_length=3000)
  image = models.URLField(null=True, blank=True)
  active = models.BooleanField(default=True)
  updated = models.DateTimeField(auto_now=True)


  def __str__(self):
      return self.title