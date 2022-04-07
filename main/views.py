from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View

from .models import *
# Create your views here.

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
        price_off = Product.objects.filter(old_price__gt=0).order_by('?')
        latest = Product.objects.all().order_by('-created')
        context = {
            'price_off':price_off[:4],
            'latest':latest[:8]
        }
        return render(request, 'index-6.html', context)


class ProductDetailPage(View):
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        context = {
            'product':product
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