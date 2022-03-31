from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField('Nomi', max_length=100)
    slug = models.SlugField('*',max_length=150, unique=True)

    def __str__(self):
        return self.name
        

class Tag(models.Model):
    name = models.CharField("Nomi", max_length=100)
    slug = models.SlugField('*',max_length=150, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='cat_products', on_delete=models.CASCADE)
    name = models.CharField("Nomi",max_length=250)
    slug = models.SlugField(max_length=250)
    image = models.ImageField(upload_to='product_images/',blank=True)
    description = models.TextField(blank=True)
    price = models.FloatField()
    old_price = models.FloatField('Avvalgi Narxi', null=True, blank=True)
    instock = models.BooleanField('Bor / Yok', default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)
    
    def __str__(self):
        return self.name
