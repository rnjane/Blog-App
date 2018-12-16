from django.db import models
from django.contrib.auth.models import User

class Categories(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Articles(models.Model):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/')
    writer = models.ForeignKey(User, related_name='articles', on_delete=models.CASCADE)
    category = models.CharField(max_length=40)

    def __str__(self):
        return self.title
