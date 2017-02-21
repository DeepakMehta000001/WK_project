from django.conf.urls import include, url
from django.contrib import admin
from .views import (
	CategoryListAPIView,
	SubCategoryByList,
	ProductByCategory,
	ProductBySubCategory
	)
urlpatterns = [
   	url(r'^$',CategoryListAPIView.as_view(),name='list'),
   #url(r'^(?P<pk>\d+)/$',CategoryListAPIView.as_view(),name='list'),
   #url(r'^(?P<categoryPK>\d+)/$',SubCategoryDetailAPIView.as_view(),name='detail'),
    url(r'^(?P<categoryPK>\d+)/$',SubCategoryByList.as_view(),name='subcategoriesByCategory'),
    url(r'^prodbycat/(?P<categoryPK>\d+)/$',ProductByCategory.as_view(),name='productsbyCategory'),
    url(r'^prodbysubcat/(?P<subcategoryPK>\d+)/$',ProductBySubCategory.as_view(),name='productsbySubCategory'),
    
    

    #url(r'^admin/', include(admin.site.urls)),
]
