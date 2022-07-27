from django.urls import reverse
from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=255, blank=True)
    slug = models.CharField(max_length=100, unique = True)
    cat_image = models.ImageField(upload_to = 'photos/categorias', blank = True) 

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    #url dinamica
    def get_url(self):  #funcion para retornar la urls de slug:category_slug
        return reverse('products_by_category', args=[self.slug]) #lo que devuelve este reverse es creando una url para cada categoria 'http://127.0.0.1:8000/store/computadora' agregandole el slug que corresponde a la categoria que selecionaste 

    def __str__(self):
        return self.category_name 
