from django.contrib import admin

from store.models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}

admin.site.register(Product, ProductAdmin) #envio las clases de Product de models.py y la clase de ProductAdmin de admin.py a Django Administration