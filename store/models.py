from django.db import models
from category.models import Category

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to = 'photo/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE) #cuando se elimine una categoria tambien se van a eliminar los productos de esa categoria
    created_date = models.DateTimeField(auto_now_add=True) 
    modified_date = models.DateTimeField(auto_now=True) 

    def __str__(self): #listar los productos por un nombre especifico
        return self.product_name
