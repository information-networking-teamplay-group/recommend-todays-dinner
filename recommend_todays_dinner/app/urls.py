from django.contrib import admin
from django.urls import path
from app import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('list/', views.list, name = 'list'),
    path('recommend/', views.recommend, name = 'recommend'),
    path('rank/', views.rank, name = 'rank'),
    path('review/', views.review, name = 'review'),
]