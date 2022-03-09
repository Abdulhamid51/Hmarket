from django.db import models
from main.views import Product

# Create your models here.



class Sold_products(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    total_price = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.product.name