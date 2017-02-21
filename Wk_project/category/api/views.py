from rest_framework.generics import ListAPIView, RetrieveAPIView
#from .urls import category_id
from category.models import CategoryModel, SubCategoryModel
from .serializers import CategorySerializer, SubCategorySerializer

class CategoryListAPIView(ListAPIView):
	queryset = CategoryModel.objects.all() 
	serializer_class = CategorySerializer


class SubCategoryListAPIView(ListAPIView):
	#lookup_field = 'categoryPK'
	#cid = kwargs['categoryPK']
	#print("lf->",lookup_field)
	serializer_class = SubCategorySerializer
	def get_queryset(self):
		return SubCategoryModel.objects.filter(categoryPK=self.kwargs['categoryPK'])
	#queryset = SubCategoryModel.objects.all()
	#serializer_class = SubCategorySerializer
	#queryset = get_query()
	

#class SubCategoryDetailAPIView(RetrieveAPIView):
#	queryset = SubCategoryModel.objects.all()
#	serializer_class = SubCategorySerializer
#	lookup_field = 'categoryPK'
	#lookup_url_kwarg = "categoryPk"
