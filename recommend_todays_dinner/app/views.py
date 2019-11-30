from django.shortcuts import render,get_object_or_404
from . import models

# Create your views here.

def lists(request):
    res = {'restaurants':models.Restaurants.objects.all()}
    return render(request,'lists/index.html', res)
    
def review(request, res_id):
    restaurants = get_object_or_404(models.Restaurants,pk=res_id)
    return render(request,'review/index.html', {'restaurants':restaurants})

def recommend(request):
    return render(request,'recommend/index.html')
    
def rank(request):
    restaurants = models.Restaurants.objects.all()
    scores = []
    index = -1

    for res in restaurants:
        review = res.review_set.all()
        scores.append(0)
        index += 1
        for rev in review:
            scores[index] += rev.score

        if(len(review) != 0):
            scores[index] /= len(review)
    
    return render(request,'rank/index.html',{'restaurants':restaurants,'scores':scores})

def index(request):
    return render(request,'index.html')