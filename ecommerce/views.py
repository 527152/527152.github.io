from django.shortcuts import render

from store.models import Product

def home(request):

    products = Product.objects.all().filter(is_available=True) #me trae todos los pruductos pero q estan activos.

    #el resultado de products va a un diccionario y en el return poner context
    context = {
        'products': products
    }

    return render(request, 'home.html', context)