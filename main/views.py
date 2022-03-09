from multiprocessing import context
from django.contrib import messages
from django.shortcuts import render, redirect

from shop.settings import BASE_DIR
from .models import Brands, Category, Product
import datetime
from datetime import timedelta, datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def is_product_new():
    for i in Product.objects.all():
        if i not in  Product.objects.filter(created_date__gt=datetime.now() - timedelta(days=15)):
            i.new = False
            i.save()
        else:
            i.new = True
            i.save()
is_product_new()
    


def index(request):
    categories = Category.objects.all()
    products = Product.objects.all().order_by('?')[:8]
    d_products = Product.objects.all().order_by('-id')[:8]
    n_products = Product.objects.filter(new=True).order_by('?')[:8]
    

    context = {
        'products': products,   
        'categories': categories,
        'd_products': d_products,
        'n_products': n_products,
    }
    return render(request, 'index.html', context)


def single_product(request, slug):
    product = Product.objects.get(slug=slug)
    related_products = Product.objects.filter(category=product.category).order_by('?')[:6]
    context = {
        'product': product,
        'r_products': related_products,
    }
    return render(request, 'single-product.html', context)



def products_page(request):
    categories = Category.objects.all()
    products = Product.objects.all().order_by('-id')
    brands = Brands.objects.all()

    # page = request.GET.get('page', 1)

    # paginator = Paginator(products, 30)
    # try:
    #     products = paginator.page(page)
    # except PageNotAnInteger:
    #     products = paginator.page(1)
    # except EmptyPage:
    #     products = paginator.page(paginator.num_pages)
    
    context = {
        'categories': categories,
        'products': products,
        'brands': brands,
    }
    return render(request, 'products.html', context)


def login(request):
    return render(request, 'login.html')



def search(request):
    categories = Category.objects.all()
    if request.method == 'POST': item = request.POST.get('item')
    products_all = []
    products = Product.objects.filter(name__icontains = item)
    for q in products: products_all.append(q)
    products1 = Product.objects.filter(characters__icontains = item)
    for w in products1: products_all.append(w)
    list1 = item.lower().split()
    for e in Category.objects.all():
        for g in list1:
            for h in e.name.split():
                if h.lower() == g: prs = Product.objects.filter(category_id=e.id); products_all.extend(prs)
    products_all = list(set(products_all))
    if len(products_all)==0: messages.info(request, 'Sorry, Nothing found for your request!')
    context = {
        'categories': categories,
        'products': products_all
    }
   
    return render(request, 'products.html', context)

    
    
def cat_brand_filter(request, category, brand):
    categories = Category.objects.all()
    category1 = Category.objects.get(name=category)
    brand1 = Brands.objects.get(name=brand)
    products = Product.objects.filter(category=category1, brand_name=brand1)
    brands = category1.brands.all()
        
    context = {
        'categories': categories,
        'products': products,
        'brands': brands,
    }
    return render(request, 'products.html', context)




def brand_cat_filter(request, brand, category):
    brands = Brands.objects.all()
    brand1 = Brands.objects.get(name=brand)
    category1 = Category.objects.get(name=category)
    products = Product.objects.filter(brand_name=brand1, category=category1)
    categories = brand1.categories.all()
        
    context = {
        'brands': brands,
        'categories': categories,
        'products': products,
    }
    return render(request, 'products.html', context)




def cat_filter(request, category):
    categories = Category.objects.all(); 
    category1 = Category.objects.get(name=category)
    products = Product.objects.filter(category=category1)
    brands = category1.brands.all()
    
    lastpath = request.META.get('HTTP_REFERER')
    for brand in Brands.objects.all():
        if brand.name in lastpath:
            return redirect(f'/brands/{brand.name}/{category}/')
        
    context = {
        'categories': categories,
        'products': products,
        'brands': brands,
    }
    return render(request, 'products.html', context)




        
def brands_filter(request, brand):
    brands = Brands.objects.all()
    brand1 = Brands.objects.get(name=brand)
    products = Product.objects.filter(brand_name=brand1)
    categories = brand1.categories.all()
    lastpath = request.META.get('HTTP_REFERER')
    for category in Category.objects.all():
        if category.name in lastpath:
            return redirect(f'/products/{category.name}/{brand}/')
    context = {
        'categories': categories,
        'products': products,
        'brands': brands
    }
    return render(request, 'products.html', context)



def product_sort(request):
    if request.method == 'GET':
        sorting = request.GET.get('sorting')
    lastpath = request.META.get('HTTP_REFERER')
    
    for brand in Brands.objects.all():
        for category in Category.objects.all():
            if brand.name in lastpath and category.name not in lastpath:
                products = Product.objects.filter(brand_name=brand)
            elif category.name in lastpath and brand.name not in lastpath:
                products = Product.objects.filter(category=category)
            elif category.name in lastpath and brand.name in lastpath:
                products = Product.objects.filter(category=category, brand_name = brand)
    
    
    if sorting == 'Name, A to Z':   
        products1 = products.order_by('name')
    elif sorting == 'Name, Z to A':
        products1 = products.order_by('created_date')
    elif sorting == 'Price, low to high':
        products1 = products.order_by('price')
    elif sorting == 'Price, high to low':
        products1 = products.order_by('-price')
    elif sorting == 'Sort By new':
        products1 = products.order_by('created_date')
    elif sorting == 'Sort By old':
        products1 = products.order_by('-created_date')
    print(lastpath)
    return redirect(request, 'products.html', {'products': products1})


# def product_filter(request):
#     print(request.POST)
#     if request.method == 'POST':
#         price = request.POST.get('productprice')
#         categories = request.POST.get('productcategory')
#         brands = request.POST.get('productbrand')
#         # price = price.replace('$', '').replace('-' '').split()
#         print(price, 'aaaaaaaaaaaaaaaaaaaaaaaaaaaa')
#         print(categories, 'bbbbbbbbbbbbbbbbbbbbb')
#         print(brands, 'ccccccccccccccccccccccccccccccc')
#         return redirect(request.META.get('HTTP_REFERER'))
        
        
        
        