from django.db import models

# Create your models here.

class Restaurant(models.Model):
    latitude = models.FloatField(default = 0)
    longitude = models.FloatField(default = 0)
    name = models.CharField(max_length = 20)
    lore = models.CharField(max_length = 500)

    def __str__(self):
        return self.name