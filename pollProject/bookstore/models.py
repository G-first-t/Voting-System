from django.db import models

# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=300)
    description=models.TextField()
    pages=models.IntegerField()

    def __str__(self):
        return self.title