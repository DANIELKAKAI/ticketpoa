from django.shortcuts import render

# Create your views here.

def merchant(request):
	return render(request,'dashboard/merchant.html',{})

def merchant_account(request):
	return render(request,'dashboard/merchant_account.html',{})

def merchantfinance(request):
	return render(request,'dashboard/merchantfinance.html',{})

def merchantproducts(request):
	return render(request,'dashboard/merchantproducts.html',{})

def merchantprofile(request):
	return render(request,'dashboard/merchantprofile.html',{})

def merchantstores(request):
	return render(request,'dashboard/merchantstores.html',{})

def merchantusers(request):
	return render(request,'dashboard/merchantusers.html',{})

def newstore(request):
	return render(request,'dashboard/newstore.html',{})

def orders(request):
	return render(request,'dashboard/orders.html',{})
