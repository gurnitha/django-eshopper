from django.shortcuts import render

from apps.home.models import Category

# Create your views here.

# # Homepage view 1
# def Homepage(request):
# 	return render(request, 'home/index.html')

# Homepage view 2
def Homepage(request):

	categories = Category.objects.all()

	context = {
		'categories':categories
	}
	
	return render(request, 'home/index.html', context)