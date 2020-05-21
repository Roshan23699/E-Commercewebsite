from django.shortcuts import render
from django.http import HttpResponse
from .models import SlideShow
from math import ceil
from .models import Product
import re
from users.models import Cart, Orders, Profile
from django.contrib.auth.models import User
import smtplib 
from email.message import EmailMessage
# Create your views here.


def index(request):
	allProds = []
	catx = Product.objects.values('category')
	cats = {item['category'] for item in catx}
	for cat in cats:
		product = Product.objects.filter(category=cat)
		allProds.append([cat, product])

	# allProds = [params, params, params]
	if(request.user.is_authenticated):
		carx = len(Cart.objects.filter(user=request.user))
	else : 
		carx = None
	params = {'list' : allProds, 'slides': SlideShow.objects.all(), 'cart':carx }
	return render(request, 'shop/index.html', params)


def grocery(request):
	if(request.user.is_authenticated):
		carx = len(Cart.objects.filter(user=request.user))
	else : 
		carx = None
	allProds = []
	catx = Product.objects.values('category')
	cats = {item['category'] for item in catx}
	for cat in cats:
		product = Product.objects.filter(category=cat)
		allProds.append([cat, product])

	# allProds = [params, params, params]
	params = {'list': allProds, 'slides': SlideShow.objects.all(), 'cart': carx}
	return render(request, 'shop/grocery.html', params)


def fruits(request):
	if(request.user.is_authenticated):
		carx = len(Cart.objects.filter(user=request.user))
	else : 
		carx = None
	allProds = []
	catx = Product.objects.values('category')
	cats = {item['category'] for item in catx}
	for cat in cats:
		if cat == 'Fruit':
			product = Product.objects.filter(category=cat)
			allProds.append([cat, product])
			params = {'list' : allProds, 'slides': SlideShow.objects.all(), 'cart': carx}
	return render(request, 'shop/fruits.html', params)


def vegetables(request):
	if(request.user.is_authenticated):
		carx = len(Cart.objects.filter(user=request.user))
	else : 
		carx = None
	allProds = []
	catx = Product.objects.values('category')
	cats = {item['category'] for item in catx}
	for cat in cats:
		if cat == 'vegetables':
			product = Product.objects.filter(category=cat)
			allProds.append([cat, product])
			params = {'list' : allProds, 'slides': SlideShow.objects.all(), 'cart': carx}
	return render(request, 'shop/vegetables.html', params)


def search_results(request):
	if(request.user.is_authenticated):
		carx = len(Cart.objects.filter(user=request.user))
	else : 
		carx = None
	search = request.GET.get('Search', 'default')
	products = Product.objects.all()
	a = []

	for i in products:
		if re.search(search, i.product_name, re.IGNORECASE):
			a.append(i)
	params = {'list': a, 'cart': carx}
	return render(request, 'shop/search.html', params)


def about(request):
	if(request.user.is_authenticated):
		carx = len(Cart.objects.filter(user=request.user))
	else : 
		carx = None
	return render(request, 'shop/about.html')


def contact(request):
	if(request.user.is_authenticated):
		carx = len(Cart.objects.filter(user=request.user))
	else : 
		carx = None
	return HttpResponse('we are at contact')


def tracker(request):
	if(request.user.is_authenticated):
		carx = len(Cart.objects.filter(user=request.user))
	else : 
		carx = None
	return HttpResponse('we are at tracker')


def search(request):
	if(request.user.is_authenticated):
		carx = len(Cart.objects.filter(user=request.user))
	else : 
		carx = None
	return HttpResponse('we are at search')


def productview(request, cat):
	if(request.user.is_authenticated):
		carx = len(Cart.objects.filter(user=request.user))
	else : 
		carx = None
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
	
	return render(request, 'shop/productview.html', {'list': a, 'cart': carx})


def order(request):
	if(request.user.is_authenticated):
		carx = len(Cart.objects.filter(user=request.user))
	else : 
		carx = None
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.starttls() 
	s.login("myawesomecart@gmail.com", "MyAwesomeCart@123")
	msg = EmailMessage()
	subject = "Mail regarding your Recent Order"
	message = "Dear " + str(request.user) + ", ordered products will be delivered to you within 2-3 working days."
	message = message + "\n"
	message = message + "Your Order:"
	message = message + "\n"
	cart = Cart.objects.filter(user=request.user)
	n = len(cart)
	list1 = []
	order = Orders()
	order.user = request.user
	order.product_name = 'default'
	sum1 = 0
	for car in cart:
		orderr = Orders()
		orderr.product_id = car.product_id
		orderr.user = request.user
		orderr.quantity = car.quantity
		orderr.category = car.category
		orderr.subcategory = car.subcategory
		orderr.price = car.price * car.quantity
		orderr.image = car.image
		orderr.product_name = car.product_name
		orderr.save()
		list1.append(orderr)
		sum1 = sum1 + car.price * car.quantity
		message = message + f"Product : {orderr.product_name}\tQuantity: {orderr.quantity}\tPrice: {orderr.price}\n"
	cart.delete()
	order.price = sum1
	profile = Profile.objects.filter(user=request.user).first()
	order.shipped = profile.address
	order.save()
	message = message + "\n"
	message = message + f"Total Price: {sum1}"
	message = message + "\n"
	message = message + " Thank you for using MyAwesomeCart.\n"
	msg.set_content(message)
	msg['Subject'] = subject
	msg['From'] = "myawesomecart@gmail.com"
	msg['To'] = request.user.email
	s.send_message(msg)
	s.quit()
	return render(request, 'shop/checkout.html', {'cart':len(Cart.objects.all()), 'list1': list1})
