from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=150)

	def __str__(self):
		return self.name



class SubCategory(models.Model):
	name = models.CharField(max_length=150)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	def __str__(self):
		return self.name



class Product(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, default='')
	subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=False, default='')
	name = models.CharField(max_length=150)
	price = models.IntegerField()
	image = models.ImageField(upload_to='products/img')
	data = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.name