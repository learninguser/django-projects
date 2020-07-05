from django.shortcuts import render
from django.views import generic

# Create your views here.

class HomePageView(generic.TemplateView):
    template_name = 'store/store.html'

class CheckoutView(generic.TemplateView):
    template_name = 'store/checkout.html'

class CartView(generic.TemplateView):
    template_name = 'store/cart.html'