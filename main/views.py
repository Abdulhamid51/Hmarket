from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
# Create your views here.

class ExampleView(View):
    def get(self,request):
        return JsonResponse({'salom':'<h1>salom<h1/>'})