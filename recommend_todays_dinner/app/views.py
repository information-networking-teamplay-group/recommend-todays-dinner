from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import models
import math

# Create your views here.

def lists(request):
    res = {'restaurants':models.Restaurants.objects.all()}
    return render(request,'lists/index.html', res)
    
def review(request, res_id):
    restaurants = get_object_or_404(models.Restaurants,pk=res_id)
    tags = restaurants.tags.split('|')

    return render(request,'review/index.html', {'restaurants':restaurants, 'tags',tags})

def review_submit(request, res_id):
    restaurants = get_object_or_404(models.Restaurants, pk=res_id)
    new_writer = request.POST['name']
    new_score = request.POST['score']
    new_contents = request.POST['contents']
    new_review = models.Review(writer=new_writer, score=new_score, contents=new_contents, restaurant=restaurants)
    new_review.save()
    return HttpResponseRedirect(reverse('app:review', args=(restaurants.id,)))

def recommend(request):
    res = {'restaurants':models.Restaurants.objects.all(), 'last_tag':''}

    return render(request,'recommend/index.html', res)

def recommend_filter(request):
    restaurants = models.Restaurants.objects.all()
    last_tag = request.POST['last_tag']
    new_tag = request.POST['new_tag']
    tags = last_tag
    if tags == '':
        tags = new_tag
    else:
        tags = tags + "|" + new_tag

    tag_list = tags.split('|')

    restaurants_value = restaurants.values()
    restaurants_filter = []

    for res in restaurants_value:
        res_tag = res['tags'].split('|')
        asdf = True

        for tag in tag_list:
            if tag not in res_tag:
                asdf = False

        if asdf == True:
            restaurants_filter.append(res)

    return render(request,'recommend/index.html', {'restaurants':restaurants_filter, 'last_tags':tags})
    
def rank(request):
    restaurants = models.Restaurants.objects.all()
    index = -1

    restaurants_value = restaurants.values()
    scores = []

    for res in restaurants:
        review = res.review_set.all()
        scores.append(0)
        index += 1

        for rev in review:
            scores[index] += rev.score

        if(len(review) != 0):
            scores[index] /= len(review)

    index = 0
    for res in restaurants_value:
        res['score'] = math.floor(scores[index] * 100) / 100
        index += 1

    restaurants_value = sorted(restaurants_value, key=lambda res: res['score'], reverse=True)

    return render(request,'rank/index.html',{'restaurants':restaurants_value})

def index(request):
    return render(request,'index.html')