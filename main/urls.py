from django.urls import path
from .views import brand_cat_filter, brands_filter, cat_brand_filter, cat_filter, index, login, products_page, search, single_product


urlpatterns = [
    path('', index, name='index'),
    path('product/<str:slug>/', single_product, name='single_product'),
    path('products_all/', products_page, name='products_page'),
    path('products/<str:category>/', cat_filter, name='cat_filter'),
    path('brands/<str:brand>/', brands_filter, name='brands_filter'),
    
    path('products/<str:category>/<str:brand>/', cat_brand_filter, name='cat_brand_filter'),
    path('brands/<str:brand>/<str:category>/', brand_cat_filter, name='brand_cat_filter'),
    # path('product_filter/', product_filter, name='product_filter'),
    
    path('login', login, name='login'),
    path('search/', search, name='search'),
    
]
