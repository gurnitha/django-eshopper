from django.shortcuts import render

from apps.home.models import Category, Product

# Create your views here.

# # Homepage view 1
# def Homepage(request):
# 	return render(request, 'home/index.html')

# # Homepage view 2
# def Homepage(request):

# 	categories = Category.objects.all()

# 	context = {
# 		'categories':categories,
# 		'products':products
# 	}
	
# 	return render(request, 'home/index.html', context)


# Homepage view 3
def Homepage(request):

	categories = Category.objects.all()

	"""
	Fetching a product that belong to a category and subcategory

	<li><a href="/?category={{category.id}}">{{subcat.name}} </a></li>
	http://127.0.0.1:8000/?category=2	
	"""
	# Step 1: Get category and assign it as categoryId
	categoryId = request.GET.get('category') # <-- line 32 (?/category)
	# Step 2: If there is categoryId
	if categoryId:
		# Step 3: Filter the product where subcategory=categoryId
		#         and assign it as products 
		products = Product.objects.filter(subcategory=categoryId)
	# Step 4: If Step 1 to 3 not found, return all products
	else:
		products = Product.objects.all()

	context = {
		'categories':categories,
		'products':products
	}
	
	return render(request, 'home/index.html', context)


