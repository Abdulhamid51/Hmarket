from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from cart.models import Order

from .models import *
# Create your views here.

def loginRegister(request):
    return render(request, 'login-register.html')

def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        lang = request.POST.get('lang')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if lang == 'ru':
                return redirect(f'/{lang}')
            else:
                return redirect('/')
        else:
            if lang == 'ru':
                return redirect(f'/{lang}')
            else:
                return redirect('/')

def logoutview(request):
    if request.user.username:
        request.session.flush()
        return redirect('/')
    else:
        return redirect('main:login')


def registerview(request):
    if request.method == 'POST':
        first = request.POST.get('first_name')
        last = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        lang = request.POST.get('lang')
        print(password)
        new_user = User.objects.create_user(
            first_name=first,
            last_name=last,
            username=username,
            password=password
        )
        my_profile = MyUser.objects.get(user=new_user)
        my_profile.phone = phone
        my_profile.address = address
        my_profile.save()
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if lang == 'ru':
                return redirect(f'/{lang}')
            else:
                return redirect('/')
        else:
            if lang == 'ru':
                return redirect(f'/{lang}')
            else:
                return redirect('/')

@login_required
def order(request):
    pro_id = request.GET.get('id')
    quantity = request.GET.get('quantity')
    product = Product.objects.get(id=int(pro_id))
    user = request.user
    price = product.price*int(quantity)
    Order.objects.create(
        user=user,
        product=product,
        all_price=price,
        quantity=quantity
    )
    return JsonResponse({
        'Ismi':user.first_name,
        'Familiyasi':user.last_name,
        'Manzil':user.myuser.address,
        'Telefon':user.myuser.phone,
        'Tovar manzili':f"http://imaxmebel.uz/product/{product.slug}"
    })

def change_lang(request):
    current = request.GET.get('now')
    lang = request.GET.get('lang')
    next = request.GET.get('next')
    next_to_uz = next.replace('/ru/','')

    if current == lang:
        return redirect(next)
    else:
        if lang == 'uz':
            return redirect(f'/{next_to_uz}')
        else:
            return redirect('/ru'+next)

class IndexPageView(View):
    def get(self,request):
        slider = Slider.objects.all()
        price_off = Product.objects.filter(old_price__gt=0).order_by('?')
        latest = Product.objects.all().order_by('-created')
        last = Slider.objects.last()
        context = {
            'price_off':price_off[:4],
            'latest':latest[:8],
            'slider':slider[:3],
            'last':last
        }
        return render(request, 'index-6.html', context)


class ProductsView(View):
    def get(self,request):
        products = Product.objects.filter(instock=True).order_by('?')
        context = {
            'products':products
        }
        return render(request, 'shop.html', context)


class AboutUs(View):
    def get(self,request):
        return render(request, 'about-us.html')


class ContactUs(View):
    def get(self,request):
        return render(request, 'contact-us.html')


class ProductDetailPage(View):
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        other = Product.objects.all().order_by('?')
        context = {
            'product':product,
            'other':other[:8]
        }
        return render(request, 'product-details.html', context)


class CategoryDetailPage(View):
    def get(self, request, slug):
        category = get_object_or_404(Category, slug=slug)
        products = Product.objects.filter(category=category)
        context = {
            'category':category.name,
            'products':products
        }
        return render(request, 'category.html', context)