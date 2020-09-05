"""crm1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('account.urls')) 
]

# decirle a django que hace con un path camino
# 2. encontrar el pattern  que el usuario coloco en el navegador debe retornar
# la pagina que busca el usuario , la rta puede ser response http apidata json o TEMPLATES
# coloque comentario pq en si aca no se hace el llamado de urls s ehac ene el proyecto
