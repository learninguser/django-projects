from django.urls import path, include
from store.views import HomePageView, CartView, CheckoutView

urlpatterns = [
    path('', HomePageView.as_view(), name='store'),
    path('cart/', CartView.as_view(), name='cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
]