from category.models import Category
from django.shortcuts import get_object_or_404, render
from store.models import Product

# Create your views here.

def store(request, category_slug=None):

    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)#Devuelve un objeto especificado de un modelo en función de su valor de clave principal y genera una excepción Http404 (not found) si el registro no existe
        products = Product.objects.filter(category=categories, is_available=True)#filtra los products que estan activos
        product_count = products.count()
    else:

        products = Product.objects.all().filter(is_available=True) #trae todos los productos que estan activos
        product_count = products.count() #cantidad de productos que hay en la base de datos

    #diccionario donde estan los productos que estan activos y su cantidad
    context = {
        'products' : products,
        'product_count' : product_count,
    }

    return render(request, 'store.html', context)