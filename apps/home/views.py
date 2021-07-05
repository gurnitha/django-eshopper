from django.shortcuts import render

from apps.home.models import Category, Product

# Create your views here.

# # Homepage view 1
# def Homepage(request):
# 	return render(request, 'home/index.html')

# Homepage view 2
def Homepage(request):

	categories = Category.objects.all()
	products   = Product.objects.all()

	context = {
		'categories':categories,
		'products':products
	}
	
	return render(request, 'home/index.html', context)