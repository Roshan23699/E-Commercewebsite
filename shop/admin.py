from django.contrib import admin

# Register your models here.
from .models import Product
from .models import SlideShow

admin.site.register(SlideShow)
admin.site.register(Product)

