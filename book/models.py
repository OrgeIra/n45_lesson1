from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()

    def __str__(self):
        return self.name

# Create your models here.
