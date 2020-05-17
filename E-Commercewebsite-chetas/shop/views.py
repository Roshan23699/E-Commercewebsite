from django.shortcuts import render
from django.http import HttpResponse
from .models import SlideShow
from math import ceil
from .models import Product

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

def about(request):
	return render(request, 'shop/about.html')

def contact(request):
	return HttpResponse('we are at contact')

def tracker(request):
	return HttpResponse('we are at tracker')

def search(request):
	return HttpResponse('we are at search')

def productview(request):
	return HttpResponse('we are at productview')

def checkout(request):
	return HttpResponse('we are at checkout') 


