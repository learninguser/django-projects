from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    statuses = [("D","Draft"),("P","Published")]

    title = models.CharField(max_length = 250, unique=True)
    content = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    status = models.CharField(max_length=1,choices=statuses,default="D")

    def __str__(self):
        return self.title