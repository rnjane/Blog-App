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

    def validate_category(self, value):
        '''validate category is from an existing category'''
        categories = []
        for category in list(models.Categories.objects.all()):
            categories.append(category.name)
        for category_name in categories:
            if category_name in value.lower():
                return value
            raise serializers.ValidationError("Use an existing category, or create a new one. The existing ones are: {0} ".format(categories))
