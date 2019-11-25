from django.urls import path
from review import views

app_name = 'review'
urlpatterns = [
    path('<int:restaurant_id>/', views.index, name='index'),
]