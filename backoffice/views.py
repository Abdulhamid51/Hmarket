from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from main.models import Brands, Category, Product
from .models import Sold_products
import datetime
# Create your views here.



@staff_member_required
def qrcodes_page(request):
    products = Product.objects.all()
    
    return render(request, 'qrcodes.html', {'products':products})



@staff_member_required
def index(request):
    sold_products = Sold_products.objects.filter(date__gt=datetime.datetime.now() - datetime.timedelta(days=1))
    
    context = {
        'sold_products': sold_products,
    }
    return render(request, 'backoffice/index.html', context)


@staff_member_required
def products(request):
    products = Product.objects.all()
    
    
    context = {
        'products': products
    }
    return render(request, 'backoffice/tables.html', context)


@staff_member_required
def add_product(request):
    categories = Category.objects.all()
    brands = Brands.objects.all()
    
    
    context = {
        'categories': categories,
        'brands': brands,
    }
    return render(request, 'backoffice/add_product.html', context)


@staff_member_required
def adds_product(request):
    if request.method == 'POST':
        r = request.POST.get
        name = r('name')
        characters = r('characters')
        category = r('category')
        brand = r('brand')
        price = r('price')
        discount = r('discount')
        rf = request.FILES.get
        image1 = rf('image1')
        image2 = rf('image2')
        image3 = rf('image3')
        image4 = rf('image4')
        image5 = rf('image5')
        
        # if image4 and not image5:
        #     Product.objects.create(name=name, characters=characters, category_id=category, brand=brand, price=price,
        #                            discount=discount, image1=image1, image2=image2, image3=image3, image4=image4)
        # elif image5 and not image4:
        #     Product.objects.create(name=name, characters=characters, category_id=category, brand=brand, price=price,
        #                            discount=discount, image1=image1, image2=image2, image3=image3, image5=image5)
        # if image4 and image5:
        Product.objects.create(name=name, characters=characters, category_id=category, brand_name_id=brand, price=price,
                                discount=discount, image1=image1, image2=image2, image3=image3, image4=image4, image5=image5)
        return redirect('add_product')
    


@staff_member_required
def product_edit(request, pk):
    product = Product.objects.get(id=pk)
    categories = Category.objects.all()
    brands = Brands.objects.all()
    
    context = {
        'product': product,
        'categories': categories,
        'brands': brands
    }
    return render(request, 'backoffice/product_edit.html', context)





@staff_member_required
def product_edits(request):
    if request.method == 'POST':
        r = request.POST.get
        name = r('name')
        product_id = r('product_id')
        characters = r('characters')
        price = r('price')
        discount = r('discount')
        category_id = r('category')
        brand_id = r('brand')
        product = Product.objects.get(id=product_id)
        category = Category.objects.get(id=category_id)
        brand = Brands.objects.get(id=brand_id)
        product.name = name
        product.characters = characters
        product.price = price
        product.discount = discount
        product.category = category
        product.brand = brand
        product.save()
        return redirect(request.META.get('HTTP_REFERER'))
    
    

@staff_member_required
def product_image_edit(request, pk):
    product = Product.objects.get(id=pk)
    
    
    context = {
        'product': product,
    }
    return render(request, 'backoffice/product_image_edit.html', context)





@staff_member_required
def product_image_edits(request):
    if request.method == 'POST':
        r = request.FILES
        product_id = request.POST.get('product_id')
        image1 = r['image1']
        image2 = r['image2']
        image3 = r['image3']
        image4 = r['image4']
        image5 = r['image5']
        product = Product.objects.get(id=product_id)
        product.image1 = image1
        product.image2 = image2
        product.image3 = image3
        product.image4 = image4
        product.image5 = image5
        product.save()
        return redirect(request.META.get('HTTP_REFERER'))
    
    
@staff_member_required
def sell_product(request, pk):
    if request.method =='GET':
        number = request.GET.get('number')
        product = Product.objects.get(id=pk)
        qoldiq = int(product.quantity) - int(number) 
        product.quantity = qoldiq
        product.save()
        total_price = int(number)*int(product.price)
        Sold_products.objects.create(product=product, quantity=number, total_price=total_price)
        return redirect(request.META.get('HTTP_REFERER'))