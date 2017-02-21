from django.db import models

# Create your models here.

class CategoryModel(models.Model):
	category_name = models.CharField(max_length=50)

	def __str__(self):
		return self.category_name

class SubCategoryModel(models.Model):
	categoryPK = models.ForeignKey(CategoryModel,on_delete=models.CASCADE)
	subcategory_name = models.CharField(max_length=50)

	def __str__(self):
		return self.subcategory_name

class ProductModel(models.Model):
	#categoryPK = models.ForeignKey(CategoryModel,on_delete=models.CASCADE)
	subcategoryPK = models.ForeignKey(SubCategoryModel,on_delete=models.CASCADE)
	product_name = models.CharField(max_length=50)

	def __str__(self):
		return self.product_name
