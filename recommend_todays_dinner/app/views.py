from django.shortcuts import render

# Create your views here.

def list(request):
    return render(request,'list/index.html')
    
def review(request):
    return render(request,'review/index.html')
    
def recommend(request):
    return render(request,'recommend/index.html')
    
def rank(request):
    return render(request,'rank/index.html')

def index(request):
    return render(request,'./templates/index.html')