from django.shortcuts import render
from django import HttpResponse # 2 urls

# Create your views here.
# clases que activan los patterns de urls

# 2 crear funciones
def home(request):
    return HttpResponse('homepage')

def contact(request):
    return HttpResponse('contactpage')

def products(request):
    return HttpResponse('products')
