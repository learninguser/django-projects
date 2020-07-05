from django.urls import path
from account import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('customer/<int:pk>', views.CustomerView.as_view(), name='customer'),
    path('customer/create/', views.CreateCustomerView.as_view(), name='createcustomer'),
    path('customer/update/<int:pk>', views.updateCustomerView.as_view(), name='updatecustomer'),
    path('products/', views.ProductView.as_view(), name='product'),
    path('order/create/', views.CreateOrderView.as_view(), name='createorder'),
    path('order/update/<int:pk>', views.OrderUpdateView.as_view(), name='updateorder'),
    path('order/delete/<int:pk>', views.OrderDeleteView.as_view(), name='deleteorder')
]