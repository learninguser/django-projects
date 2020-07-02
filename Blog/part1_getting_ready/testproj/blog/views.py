from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
# def HomePageView(request):
#     return HttpResponse('<h1>Hello World !!</h1>')

def HomePageView(request):
    return render(request, 'blog/index.html')
