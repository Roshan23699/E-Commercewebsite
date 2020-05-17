from django.shortcuts import render
from django.http import HttpResponse
from .models import SlideShow
from math import ceil
from .models import Product
import re
from users.models import Cart
from django.contrib.auth.models import User
# Create your views here.


def index(request):
	#product = Product.objects.all()
	allProds = []
	catx = Product.objects.values('category')
	cats = {item['category'] for item in catx}
	for cat in cats:
		product = Product.objects.filter(category=cat)
		allProds.append([cat, product])

	# allProds = [params, params, params]
	params = {'list' : allProds, 'slides': SlideShow.objects.all()}
	return render(request, 'shop/index.html', params)

def grocery(request):
	#product = Product.objects.all()
	allProds = []
	print("HI I am Manish\n\n\n\n\n\n\n\n\n\n\n\n")
	catx = Product.objects.values('category')
	cats = {item['category'] for item in catx}
	for cat in cats:
		product = Product.objects.filter(category=cat)
		allProds.append([cat, product])

	# allProds = [params, params, params]
	params = {'list' : allProds, 'slides': SlideShow.objects.all()}
	return render(request, 'shop/grocery.html', params)


def fruits(request):
	#product = Product.objects.all()
	allProds = []
	catx = Product.objects.values('category')
	cats = {item['category'] for item in catx}
	for cat in cats:
		if cat == 'Fruit':
			product = Product.objects.filter(category=cat)
			allProds.append([cat, product])
			params = {'list' : allProds, 'slides': SlideShow.objects.all()}
	return render(request, 'shop/fruits.html', params)

def vegetables(request):
	#product = Product.objects.all()
	allProds = []
	catx = Product.objects.values('category')
	cats = {item['category'] for item in catx}
	for cat in cats:
		if cat == 'vegetables':
			product = Product.objects.filter(category=cat)
			allProds.append([cat, product])
			params = {'list' : allProds, 'slides': SlideShow.objects.all()}
	return render(request, 'shop/vegetables.html', params)

def search_results(request):
	search = request.GET.get('Search', 'default')
	products = Product.objects.all()
	a = []

	for i in products:
		if re.search(search, i.product_name, re.IGNORECASE):
			a.append(i)
	 
	params = {'list': a}
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
	x = '^'
	x = x + cat
	print(x)
	a = []
	for i in product:
		if re.search(x, i.category):
			a.append(i)

	# setx = {item['category'] for item in product}
	# for ele in setx:
	# 	element = request.GET[ele]
	# 	if(element is not None):
	# 		list1 = Product.objects.filter(element)
	# 		break
	
	return render(request, 'shop/productview.html', {'list':a})

def checkout(request):
	
	return render(request, 'shop/checkout.html')
	


