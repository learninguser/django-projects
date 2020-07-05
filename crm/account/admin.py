from django.contrib import admin
from account.models import Customer, Product, Order, Tag

# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Order)