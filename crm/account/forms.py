from django import forms
from account.models import Product, Order, Customer 

class CreateOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer','product','status']

class CreateCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','phone','email']