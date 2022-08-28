from django.db import models


# Create your models here.


class Anime(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    url = models.CharField(max_length=2048)
    malLink = models.CharField(max_length=2048)

    def __str__(self):
        return self.title
