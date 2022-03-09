from unicodedata import name
from django.urls import path

from .views import add_product, adds_product, index, product_edit, product_edits, product_image_edit, product_image_edits, products, sell_product
from .views import qrcodes_page


urlpatterns = [
    path('', index, name='backindex'),
    path('products/', products, name='backproducts'),
    path('qrcodes/', qrcodes_page, name='qrcodes_page'),
    
    
    path('products/add/', add_product, name='add_product'),
    path('adds_product', adds_product, name='adds_product'),
    
    
    path('product_edit/<int:pk>/', product_edit, name='product_edit'),
    path('product_edits/', product_edits, name='product_edits'),
    
    
    path('product_image_edit/<int:pk>/', product_image_edit, name='product_image_edit'),
    path('product_image_edits/', product_image_edits, name='product_image_edits'),
    
    
    path('sell_product/<int:pk>/', sell_product, name='sell_product')
    
]
