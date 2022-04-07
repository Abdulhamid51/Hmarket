from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['category','name_uz','name_ru','price','old_price','instock','description','image','slug']
    list_display = ['name','price','instock']
    list_display_links = ['name','price']
    prepopulated_fields = {"slug": ("name_uz",)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['name_uz','name_ru','slug']
    prepopulated_fields = {"slug": ("name_uz",)}

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    fields = ['sub_title_uz','sub_title_ru','title_uz','title_ru','bg_image']