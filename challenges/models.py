from django.db import models

# Create your models here.


class Review(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='posts')