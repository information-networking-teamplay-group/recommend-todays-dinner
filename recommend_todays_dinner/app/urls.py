from django.contrib import admin
from django.urls import path
from app import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('lists/', views.lists, name = 'lists'),
    path('recommend/', views.recommend, name = 'recommend'),
    path('recommend/filter', views.recommend_filter, name = 'recommend_filter'),
    path('rank/', views.rank, name = 'rank'),
    path('review/<int:res_id>/', views.review, name = 'review'),
    path('review/<int:res_id>/submit/', views.review_submit, name = 'review_submit'),
]