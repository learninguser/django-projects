from django.shortcuts import render, redirect
from django.views import generic
from account.models import Product, Order, Customer
from account.forms import CreateOrderForm, CreateCustomerForm
from django.urls import reverse_lazy, reverse

# Create your views here.

class HomePageView(generic.TemplateView):
    template_name = 'account/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        orders = Order.objects.all()
        context['orders'] = orders
        
        customers = Customer.objects.all()
        context['customers'] = customers
        
        orders_delivered = Order.objects.filter(status='Delivered').count()
        context['orders_delivered'] = orders_delivered

        orders_pending = Order.objects.filter(status='Pending').count()
        context['orders_pending'] = orders_pending

        total_orders = Order.objects.all().count()
        context['total_orders'] = total_orders

        return context


class CustomerView(generic.DetailView):
    model = Customer
    template_name = 'account/customer.html'
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = kwargs['object'].order_set.all()
        context['order_count'] = context['orders'].count()
        return context

class ProductView(generic.ListView):
    model = Product
    template_name = 'account/products.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context

class CreateCustomerView(generic.CreateView):
    model = Customer
    form_class = CreateCustomerForm
    template_name = 'account/createcustomer.html'
    pk_url_kwarg = 'pk'

    def get_success_url(self):
        return reverse('home')

class updateCustomerView(generic.UpdateView):
    model = Customer
    form_class = CreateCustomerForm
    template_name = 'account/updatecustomer.html'
    pk_url_kwarg = 'pk'

    def get_success_url(self):
        if self.object.pk:
            pk = self.object.pk
        return reverse('customer',kwargs={'pk':pk})

class CreateOrderView(generic.CreateView):
    model = Order
    form_class = CreateOrderForm
    template_name = 'account/createorder.html'

    def get_success_url(self):
        return reverse('home')

class OrderUpdateView(generic.UpdateView):
    model = Order
    form_class = CreateOrderForm
    template_name = 'account/updateorder.html'
    pk_url_kwarg = 'pk'
    
    def get_success_url(self):
        return reverse('home')

class OrderDeleteView(generic.DeleteView):
    model = Order
    form_class = CreateOrderForm
    template_name = 'account/deleteorder.html'
    pk_url_kwarg = 'pk'
    
    def get_success_url(self):
        return reverse('home')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = context['order'].product
        return context