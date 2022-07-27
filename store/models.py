from django.urls import reverse
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

    def get_url(self): #generando urls para los detalles de productos dentro del 'home'
        return reverse('product_detail', args=[self.category.slug, self.slug]) #llama al product?detail pero le tiene que pasar los slug de la categoria y productos

    def __str__(self): #listar los productos por un nombre especifico en admin
        return self.product_name