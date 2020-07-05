from django.urls import path
from store.views import HomePageView, cart, checkout

urlpatterns = [
    path('', HomePageView.as_view(), name='store'),
    # path('cart/', CartView.as_view(), name='cart'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
]