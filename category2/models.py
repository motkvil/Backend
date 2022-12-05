from django.db import models
from django.db.models.base import Model

# Create your models here.
class Category2(models.Model):
  title = models.TextField(max_length=1000)
  description = models.TextField(max_length=3000)
  image = models.URLField(null=True, blank=True)
  active = models.BooleanField(default=True)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)


  def __str__(self):
      return self.title

class Comment(models.Model):


  alias = models.CharField(max_length=2000, null=True)
  content = models.TextField(max_length=1000000)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)


  def __str__(self):
      return self.alias

class Article(models.Model):
  title = models.CharField(max_length=500)
  content = models.CharField(max_length=100000)
  image = models.URLField(blank=True)
  categories = models.ManyToManyField(Category2, related_name='article', blank=True, )
  comment = models.ManyToManyField(Comment, related_name='article_comment', blank=True, )
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  def __str__(self):
      return self.title



