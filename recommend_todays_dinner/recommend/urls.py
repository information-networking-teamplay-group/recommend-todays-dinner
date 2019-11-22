from django.urls import path
from recommend import views

app_name = 'recommend'
urlpatterns = [
    path('', views.index, name='index'),
]