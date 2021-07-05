from django.contrib import admin

from apps.home.models import Category, SubCategory, Product

# Register your models here.

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)