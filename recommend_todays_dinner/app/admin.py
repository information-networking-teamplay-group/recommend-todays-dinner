from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Restaurants)
admin.site.register(models.Review)