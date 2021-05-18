"""fmart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #admin default
    path('admin/', admin.site.urls),

    #login register all in this path
    path('register/',include('register.urls')),

    #home page with navbar and base.html for all other apps
    path('',include('home.urls')),
    
    #categories
    # path('men/',include('men.urls')),
    # path('women/',include('women.urls')),
    # path('kids/',include('kids.urls')),

    #product
    path('product/',include('product.urls')),

    #productcart
    path('productcart/',include('productcart.urls')),

    #payment
    path('payment/',include('payment.urls')),
    

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)