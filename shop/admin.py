from django.contrib import admin
from .models import Product
from .models import SlideShow


class Productsordering(admin.ModelAdmin):
    list_display = ['product_name', 'category', 'subcategory', 'price']


admin.site.register(SlideShow)
admin.site.register(Product, Productsordering)

