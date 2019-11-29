from django.shortcuts import render,get_object_or_404
from . import models

# Create your views here.

def lists(request):
    res = {'restaurants':models.Restaurants.objects.all()}
    return render(request,'list/index.html',res)
    
def review(request, res_id):
    restaurants = get_object_or_404(models.Review,pk=res_id)
    try:
        reviews = restaurants.review_set.get(pk=request.POST['review'])
        return render(requst,'review/index.html',
        {'restaurants':restaurants,'reviews':reviews})
    except (KeyError,Review.DoesNotExist):
        return render(request,'review/index.html',
        {'restaurants':restaurants,'error_message':"You didn't select a choice."})  
    else:
        pass     
    
def recommend(request):
    return render(request,'recommend/index.html')
    
def rank(request):
    restaurants = models.Restaurants.objects.all()
    scores = []
    index = -1

    for res in restaurants:
        reviews = get_object_or_404(models.Review,pk=res.id)
        scores.append(0)
        index += 1
        for review in reviews:
            scores[index] += reviews.score

        scores[index] /= reviews.size
    
    return render(request,'rank/index.html',{'restaurants':restaurants,'scores':scores})

def index(request):
    return render(request,'index.html')