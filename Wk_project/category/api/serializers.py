from rest_framework.serializers import ModelSerializer

from category.models import CategoryModel, SubCategoryModel

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
		
