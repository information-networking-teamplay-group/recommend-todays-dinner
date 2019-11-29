from django.shortcuts import render,get_object_or_404
from . import models

# Create your views here.

def lists(request):
    res = {'restaurants':models.Restaurants.objects.all()}
    return render(request,'lists/index.html',res)
    
def review(request, res_id):
    restaurants = get_object_or_404(models.Restaurants,pk=res_id)
    try:
        review = restaurants.review_set.all()
        return render(request,'review/index.html',
        {'restaurants':restaurants,'review':review})
    except (KeyError,models.Review.DoesNotExist):
        return render(request,'review/index.html',
        {'restaurants':restaurants,'error_message':"리뷰가 존재하지 않습니다."})  
    else:
        pass

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

        scores[index] /= len(review)
    
    return render(request,'rank/index.html',{'restaurants':restaurants,'scores':scores})

def index(request):
    return render(request,'index.html')