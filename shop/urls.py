from django.urls import path
from .import views

urlpatterns = [
	path('', views.index, name = 'shopHome'),
	path('grocery/', views.grocery, name = 'Grocery'),
	path('fruits/', views.fruits, name = 'Fruits'),
	path('vegetables/', views.vegetables, name = 'Vegetables'),
	path('search_results/', views.search_results, name = 'search_results'),
	path('about/', views.about, name = 'AboutUs'),
	path('contact/', views.contact, name = 'ContactUs'),
	path('tracker/', views.tracker, name = 'TrackingStatus'),
	path('search/', views.search, name = 'Search'),
	path('productview/', views.productview, name = 'ProductView'),
	path('checkout/', views.checkout, name = 'Checkout'),
]