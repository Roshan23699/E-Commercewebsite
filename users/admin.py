from django.contrib import admin
from .models import Profile, Cart, Wishlist, Orders


admin.site.register(Profile)
admin.site.register(Cart)
admin.site.register(Wishlist)
admin.site.register(Orders)
