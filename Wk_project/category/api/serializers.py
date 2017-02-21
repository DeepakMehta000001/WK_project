from rest_framework.serializers import ModelSerializer

from category.models import CategoryModel, SubCategoryModel , ProductModel

class CategorySerializer(ModelSerializer):
	class Meta:
		model = CategoryModel
		fields = [
			'id',
			'category_name',
		]


class SubCategorySerializer(ModelSerializer):
	class Meta:
		model = SubCategoryModel
		fields = [
			'id',
			'categoryPK',
			'subcategory_name',
		]
		

class ProductByCategorySerializer(ModelSerializer):
	class Meta:
		model = ProductModel
		fields = [
			'id',
			'categoryPK',
			'subcategoryPK',
			'product_name',
		]
		
class ProductBySubCategorySerializer(ModelSerializer):
	class Meta:
		model = ProductModel
		fields = [
			'id',
			'categoryPK',
			'subcategoryPK',
			'product_name',
		]