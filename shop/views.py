from django.shortcuts import render
from django.http import HttpResponse
from .models import SlideShow
from math import ceil
from .models import Product
import re
from users.models import Cart, Orders
from django.contrib.auth.models import User
import smtplib 
# Create your views here.


def index(request):
	allProds = []
	catx = Product.objects.values('category')
	cats = {item['category'] for item in catx}
	for cat in cats:
		product = Product.objects.filter(category=cat)
		allProds.append([cat, product])

	# allProds = [params, params, params]
	params = {'list' : allProds, 'slides': SlideShow.objects.all(), 'cart': len(Cart.objects.filter(user=request.user))}
	return render(request, 'shop/index.html', params)


def grocery(request):
	allProds = []
	catx = Product.objects.values('category')
	cats = {item['category'] for item in catx}
	for cat in cats:
		product = Product.objects.filter(category=cat)
		allProds.append([cat, product])

	# allProds = [params, params, params]
	params = {'list': allProds, 'slides': SlideShow.objects.all(), 'cart': len(Cart.objects.filter(user=request.user))}
	return render(request, 'shop/grocery.html', params)


def fruits(request):
	allProds = []
	catx = Product.objects.values('category')
	cats = {item['category'] for item in catx}
	for cat in cats:
		if cat == 'Fruit':
			product = Product.objects.filter(category=cat)
			allProds.append([cat, product])
			params = {'list' : allProds, 'slides': SlideShow.objects.all(), 'cart': len(Cart.objects.filter(user=request.user))}
	return render(request, 'shop/fruits.html', params)


def vegetables(request):
	allProds = []
	catx = Product.objects.values('category')
	cats = {item['category'] for item in catx}
	for cat in cats:
		if cat == 'vegetables':
			product = Product.objects.filter(category=cat)
			allProds.append([cat, product])
			params = {'list' : allProds, 'slides': SlideShow.objects.all(), 'cart': len(Cart.objects.filter(user=request.user))}
	return render(request, 'shop/vegetables.html', params)


def search_results(request):
	search = request.GET.get('Search', 'default')
	products = Product.objects.all()
	a = []

	for i in products:
		if re.search(search, i.product_name, re.IGNORECASE):
			a.append(i)
	params = {'list': a, 'cart': len(Cart.objects.filter(user=request.user))}
	return render(request, 'shop/search.html', params)


def about(request):
	return render(request, 'shop/about.html')


def contact(request):
	return HttpResponse('we are at contact')


def tracker(request):
	return HttpResponse('we are at tracker')


def search(request):
	return HttpResponse('we are at search')


def productview(request, cat):
	product = Product.objects.all()
	a = []
	for i in product:
		if cat == i.category:
			a.append(i)

	# setx = {item['category'] for item in product}
	# for ele in setx:
	# 	element = request.GET[ele]
	# 	if(element is not None):
	# 		list1 = Product.objects.filter(element)
	# 		break
	
	return render(request, 'shop/productview.html', {'list': a, 'cart': len(Cart.objects.filter(user=request.user))})


def checkout(request):
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.starttls() 
	s.login("myawesomecart@gmail.com", "MyAwesomeCart@123") 
	message = "Dear " + str(request.user) + ", ordered products will be delivered to you within 2-3 working days. Thank you for using MyAwesomeCart."
	s.sendmail("myawesomecart@gmail.com", request.user.email, message)   
	s.quit()
	cart = Cart.objects.filter(user=request.user)
	n = len(cart)
	list1 = []
	for car in cart:
		# orderr = Orders(car.proguct_id, request.user, car.quantity, car.category, car.subcategory, car.price, car.image, car.product_name)
		orderr = Orders()
		orderr.product_id = car.product_id
		orderr.user = request.user
		orderr.quantity = car.quantity
		orderr.category = car.category
		orderr.subcategory = car.subcategory
		orderr.price = car.price
		orderr.image = car.image
		orderr.product_name = car.product_name
		orderr.save()
		list1.append(orderr)
	return render(request, 'shop/checkout.html', {'cart':len(Cart.objects.all()), 'list1': list1})
