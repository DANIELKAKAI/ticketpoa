from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request,"mainapp/index.html",{})

def events(request):
	return render(request,"mainapp/events.html",{})

def flights(request):
	return render(request,"mainapp/flights.html",{})

def holidays(request):
	return render(request,"mainapp/holidays.html",{})

def artwork(request):
	return render(request,"mainapp/artwork.html",{})

def movies(request):
	return render(request,"mainapp/movies.html",{})

def music(request):
	return render(request,"mainapp/music.html",{})

def books(request):
	return render(request,"mainapp/books.html",{})

def signin(request):
	return render(request,"mainapp/login.html",{})

def signup(request):
	return render(request,"mainapp/register.html",{})

def cart(request):
	return render(request,"mainapp/cart.html",{})

def checkout(request):
	return render(request,"mainapp/checkout.html",{})

def event_checkout(request):
	return render(request,"mainapp/eventcheckout.html",{})

def holidays_checkout(request):
	return render(request,"mainapp/holidays-checkout.html",{})

def contact(request):
	return render(request,"mainapp/contact.html",{})