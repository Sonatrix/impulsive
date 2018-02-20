from django.shortcuts import render

#products
def loan(request):
	return render(request, 'products/loan.html', {})

def cards(request):
	return render(request, 'products/cards.html', {})

def insurance(request):
	return render(request, 'products/insurance.html', {})

def products(request):
	return render(request, 'products/products.html', {})