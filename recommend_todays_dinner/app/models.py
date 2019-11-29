from django.db import models

# Create your models here.

class Restaurants(models.Model):
    latitude = models.FloatField(default = 0)   #위도
    longitude = models.FloatField(default = 0)  #경도
    name = models.CharField(max_length = 20)    #식당 이름
    lore = models.CharField(max_length = 500)   #식당 설명
    tags = models.CharField(max_length = 50)    #태그

    def __str__(self):
        return self.name

class Review(models.Model):
    writer = models.CharField(max_length = 20)                          #작성자
    contents = models.CharField(max_length = 500)                       #작성자 내용
    score = models.IntegerField(default = 0)                            #작성자 별점
    restaurant = models.ForeignKey(Restaurants, on_delete = 'CASCADE')  #어느 레스토랑 리뷰인지