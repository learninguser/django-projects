from django.shortcuts import render
from blog.models import Post, Category
# from django.http import HttpResponse

# Create your views here.
# def HomePageView(request):
#     return HttpResponse('<h1>Hello World !!</h1>')

def HomePageView(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})

def PostDetailView(request, id):
    post = Post.objects.get(id = id)
    return render(request, 'blog/blogpost.html', context={'post': post})