from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')

def new_post(request):
    return render(request, 'main/new_post.html')

def new(request):
    return HttpResponse('<h1>Это вторая страница проекта на django</h1>')

def index_view(request):
    return render(request, 'main/index.html')

