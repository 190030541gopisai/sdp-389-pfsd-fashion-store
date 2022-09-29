from django.shortcuts import render

from product.models import Product
from django.db.models import Q
# Create your views here.


def search(request):
    query = request.GET['query']
    print("query = ",query)
    products = Product.objects.filter(Q(p_name__icontains=query) | Q(p_description__icontains=query))    
    count_products = len(products)

    template_name="search/search.html"
    context = {
        'products':products,
        'count':count_products
    }
    return render(request, template_name, context)


