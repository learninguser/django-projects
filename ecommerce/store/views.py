from django.shortcuts import render
from django.views import generic
from store.models import Customer, Product, Order

# Create your views here.

class HomePageView(generic.ListView):
    model = Product
    template_name = 'store/store.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context

# class CartView(generic.DetailView):
#     model = Order
#     template_name = 'store/cart.html'
#     pk_url_kwarg = 'pk'

#     def get(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             customer = request.user.customer
#             order, created = Order.objects.get_or_create(customer=customer, complete=False)
#             items = order.orderitem_set.all()
#         else:
#             items = []
#         print(self.get_queryset())
#         context = {'items':items}
#         return context

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    
    return render(request, 'store/cart.html',context={'items':items, 'order':order})


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    
    return render(request, 'store/checkout.html',context={'items':items, 'order':order})

# class CheckoutView(generic.TemplateView):
#     template_name = 'store/checkout.html'