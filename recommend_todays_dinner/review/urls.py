from django.urls import path
from review import views

app_name = 'review'
urlpatterns = [
    path('', views.index, name='index.html'),
]