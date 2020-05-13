from django.shortcuts import render
from django.http import HttpResponse
from .models import SlideShow
from math import ceil
from .models import Product
from .models import SlideShow
from .models import FoodGrain
from .models import SaltSugarandJaggery
from .models import OilsGheeandMasala
from .models import DalandPulses
from .models import Fruit
from .models import Vegetable
# Create your views here.


def index(request):
	# product = Product.objects.all()
	allProds = []
	"""catx = Product.objects.values('category')
	cats = {item['category'] for item in catx}
	for cat in cats:
		product = Product.objects.filter(category=cat)
		n = len(product)
		nSlides = n // 4 + ceil((n / 4) - (n // 4))
		lenth = range(1, nSlides + 1)
		params = [nSlides, lenth, product]
		allProds.append([nSlides, lenth , product])"""

	# allProds = [params, params, params]
	params = {'list' : allProds, 'slides': SlideShow.objects.all(), 'foodgrain' : FoodGrain.objects.all(), 'saltsugjag': SaltSugarandJaggery.objects.all(), 'oilgheemasala':OilsGheeandMasala.objects.all(), 'dalpulses': DalandPulses.objects.all()}
	return render(request, 'shop/index.html', params)

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


