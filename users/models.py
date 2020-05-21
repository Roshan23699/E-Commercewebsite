from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.utils import timezone
from shop.models import Product


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to='profile_pics')
    address = models.TextField(blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'


class Cart(models.Model):
    product_id = models.IntegerField(default=0)
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='scores',)
    quantity = models.IntegerField(default=0)
    category = models.CharField(max_length=300, default='')
    subcategory = models.CharField(max_length=300, default='')
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='shop/images', default='')
    product_name = models.CharField(max_length=30)

    def __str__(self):
        return f"Product: {self.product_name}        User:{self.user}"


class Wishlist(models.Model):
    product_id = models.IntegerField(default=0)
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='scores1',)
    quantity = models.IntegerField(default=0)
    category = models.CharField(max_length=300, default='')
    subcategory = models.CharField(max_length=300, default='')
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='shop/images', default='')
    product_name = models.CharField(max_length=30)

    def __str__(self):
        return f"Product: {self.product_name}        User:{self.user}"


class Orders(models.Model):
    # def __unicode__(self, product_id, user, quantity, category, subcategory, price, image, product_name):
    #     self.product_id = product_id
    #     self.user = user
    #     self.quantity = quantity
    #     self.category = category
    #     self.subcategory = subcategory
    #     self.price = price
    #     self.image = image
    #     self.product_name = product_name

    product_id = models.IntegerField(default=0)
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='scores2',)
    quantity = models.IntegerField(default=0)
    category = models.CharField(max_length=300, default='')
    subcategory = models.CharField(max_length=300, default='')
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='shop/images', default='')
    product_name = models.CharField(max_length=30)
    date = models.DateTimeField(default=timezone.now)
    shipped = models.CharField(max_length=300, default='')
    iscancelled = models.BooleanField(default=False)
    def __str__(self):
        return f"Product: {self.product_name}        User:{self.user}"


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)
