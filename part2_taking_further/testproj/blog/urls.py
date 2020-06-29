from django.urls import path, include
from blog import views

urlpatterns = [
    path('',views.HomePageView, name='home'),
    path('post/<int:id>', views.PostDetailView, name='post-detail'),
]