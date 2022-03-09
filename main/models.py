from email.policy import default
import os
from django.db.models.signals import pre_save, post_save
from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE
from django_extensions.db.fields import AutoSlugField
import pyqrcode
from django.dispatch import receiver
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent


class Category(models.Model):
    name = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name



class Brands(models.Model):
    name = models.CharField(max_length=30, unique=True)
    categories = models.ManyToManyField(Category, related_name='brands')
    
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150)
    characters = models.TextField()
    category = models.ForeignKey(Category, related_name='product', on_delete=CASCADE)
    brand_name = models.ForeignKey(Brands, related_name='product1', on_delete=CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(default=0)
    image1 = models.ImageField(upload_to='products/')
    image2 = models.ImageField(upload_to='products/')
    image3 = models.ImageField(upload_to='products/')
    image4 = models.ImageField(upload_to='products/', blank=True)
    image5 = models.ImageField(upload_to='products/', blank=True)
    # old_price = models.PositiveIntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    new = models.BooleanField(default=True, null=True, blank=True)
    slug = AutoSlugField(blank=True, unique=True, populate_from=['name', 'characters', 'category'])
    qrcode = models.CharField(blank=True, null=True, max_length=400)

    
    def __str__(self):
        return self.name
        
    

    
class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    
    def __str__(self):
        return self.product.name
    

@receiver(post_save, sender=Product)
def QRcode_receiver(sender, instance, created, *args, **kwargs):
    if created:
        img  = pyqrcode.create(f'http://127.0.0.1:8000/{instance.slug}')
        url_text = f'media/product_qrcodes/{instance.slug}.png'
        img.png(url_text, scale=5)
        product = Product.objects.get(id=instance.id)
        product.qrcode = f'/{url_text}'
        product.save()
    
