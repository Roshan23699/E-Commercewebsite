from django.contrib import admin
from .models import Profile, Cart, Wishlist, Orders


def make_delivered(modeladmin, request, queryset):
    queryset.update(isdelivered=True)


make_delivered.short_description = "Mark selected options as delivered"


class Orderadmin(admin.ModelAdmin):
    list_display = ['user', 'product_name', 'quantity', 'price']
    actions = [make_delivered]


admin.site.register(Profile)
admin.site.register(Cart)
admin.site.register(Wishlist)
admin.site.register(Orders, Orderadmin)
