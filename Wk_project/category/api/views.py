from rest_framework.generics import ListAPIView, CreateAPIView
#from .urls import category_id
from category.models import CategoryModel, SubCategoryModel,ProductModel

from .serializers import (
		CategorySerializer, 
		ProductByCategorySerializer, 
		SubCategorySerializer,
		ProductBySubCategorySerializer,
		ProductCreateSerializer,
		)

class CategoryListAPIView(ListAPIView):
	queryset = CategoryModel.objects.all() 
	serializer_class = CategorySerializer


class SubCategoryByList(ListAPIView):
	serializer_class = SubCategorySerializer
	def get_queryset(self):
		return SubCategoryModel.objects.filter(categoryPK=self.kwargs['categoryPK'])


class ProductByCategory(ListAPIView):
	serializer_class = ProductByCategorySerializer
	def get_queryset(self):
		return ProductModel.objects.filter(categoryPK=self.kwargs['categoryPK'])


class ProductBySubCategory(ListAPIView):
	serializer_class = ProductBySubCategorySerializer
	def get_queryset(self):
		return ProductModel.objects.filter(subcategoryPK=self.kwargs['subcategoryPK'])

class ProductCreateAPIView(CreateAPIView):
	queryset = ProductModel.objects.all() 
	serializer_class = ProductCreateSerializer


#class SubCategoryDetailAPIView(RetrieveAPIView):
#	queryset = SubCategoryModel.objects.all()
#	serializer_class = SubCategorySerializer
#	lookup_field = 'categoryPK'
	#lookup_url_kwarg = "categoryPk"
