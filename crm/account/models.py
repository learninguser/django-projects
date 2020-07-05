from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length = 200, null=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    choices = (['Indoor', 'Indoor'], ['Outdoor', 'Outdoor'])
    name = models.CharField(max_length = 200, null=True)
    price = models.FloatField(max_length = 200, null=True)
    category = models.CharField(max_length=200, choices=choices,default="Outdoor")
    description = models.CharField(max_length = 200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length = 200, null=True)
    phone = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    statuses = (['Delivered', 'Delivered'], ['Pending', 'Pending'], ['Out for Delivery', 'Out for Delivery'])
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=200, choices=statuses,default="Delivered")
    date_created = models.DateTimeField(auto_now_add=True)