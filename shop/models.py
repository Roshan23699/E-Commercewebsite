from django.db import models

# Create your models here.

class Product(models.Model):
	product_id = models.AutoField
	product_name = models.CharField(max_length=30)
	"""desc = models.CharField(max_length=300, default =)
	pub_date = models.DateField(default = '')"""
	category = models.CharField(max_length=300, default='')
	subcategory = models.CharField(max_length=300, default='')
	price = models.IntegerField(default=0)
	image = models.ImageField(upload_to='shop/images', default='')
	def __str__(self):
		return self.product_name

class SlideShow(models.Model):
	image_id = models.AutoField
	image_name = models.CharField(max_length=30)
	image = models.ImageField(upload_to='shop/images', default='')
	def __str__(self):
		return self.image_name

