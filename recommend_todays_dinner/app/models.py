from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Restaurant(models.Model):
    latitude = models.FloatField(default = 0)
    longitude = models.FloatField(default = 0)
    name = models.CharField(max_length = 20)
    lore = models.CharField(max_length = 500)
    tags = ArrayField(models.CharField(max_length=200), blank=True)

    def __str__(self):
        return self.name