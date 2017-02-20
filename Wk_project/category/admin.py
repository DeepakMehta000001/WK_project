from django.contrib import admin
from django.db import models
# Register your models here.
from .models import CategoryModel,SubCategoryModel,ProductModel

class CategoryModelAdmin(admin.ModelAdmin):
	category_display = ['category_name']
	class meta:
		model = CategoryModel

class SubCategoryModelAdmin(admin.ModelAdmin):
	subcategory_display = ['subcategory_name']
	class meta:
		model = SubCategoryModel

class ProductModelAdmin(admin.ModelAdmin):
	product_display = ['product_name']
	class meta:
		model = ProductModel


admin.site.register(CategoryModel,CategoryModelAdmin)
admin.site.register(SubCategoryModel,SubCategoryModelAdmin)
admin.site.register(ProductModel,ProductModelAdmin)