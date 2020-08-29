# 2 yo te cree
from django.urls import path
from . import views   # importo views.py d ela carpeta acounts

urlpatterns = [
    path('',views.home),
    path('about/',views.contact),
    path('products/',views.products),
]
