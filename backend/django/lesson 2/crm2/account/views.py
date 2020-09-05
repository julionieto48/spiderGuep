from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# clases que activan los patterns de urls

# 2 crear funciones
def home(request):
    return render(request, 'accounts/dashboard.html')  # usar la funcion render

def products(request):
    return render(request, 'accounts/products.html')

def customer(request):
    return render(request, 'accounts/customer.html')


# la estructura del archivo es...
#.. account
#...templates
#.... accounts
#..... .html
#..crm1

# entornos virtuales y correr Django
#https://stackoverflow.com/questions/55142774/how-to-activate-virtual-environment-in-django
#https://stackoverflow.com/questions/47880626/django-manage-py-runserver-invalid-syntax
#https://stackoverflow.com/questions/47880626/django-manage-py-runserver-invalid-syntax
