from rest_framework import serializers
from .models import Category2, Article, Comment

class Category2Serializers(serializers.ModelSerializer):
    class Meta:
        model = Category2
        fields = ('__all__')

class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('__all__')

class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('__all__')