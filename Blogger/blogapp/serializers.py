from rest_framework import serializers
from django.contrib.auth.models import User
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Categories
        fields = ['name']


class ArticlesSerializer(serializers.ModelSerializer):
    writer = serializers.ReadOnlyField(source='writer.username')
    class Meta:
        model = models.Articles
        fields = ['title', 'writer', 'content', 'category', 'image']