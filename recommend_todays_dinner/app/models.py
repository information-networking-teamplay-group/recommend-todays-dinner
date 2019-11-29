from django.db import models

# Create your models here.

class Restaurants(models.Model):
    latitude = models.FloatField(default = 0)
    longitude = models.FloatField(default = 0)
    name = models.CharField(max_length = 20)
    lore = models.CharField(max_length = 500)
    tags = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class Review(models.Model):
    writer = models.CharField(max_length = 20)
    contents = models.CharField(max_length = 500)
    score = models.IntegerField(default = 0)
    restaurant = models.ForeignKey(Restaurants, on_delete = 'CASCADE')