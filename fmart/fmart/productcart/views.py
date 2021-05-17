from django.shortcuts import render,redirect,HttpResponse,Http404

from django.contrib.auth.decorators import login_required
from .models import Cart
from home.models import Product
from django.views.generic import (
    TemplateView
)

# Create your views here.

# class CartView(TemplateView):
#     template_name = 'productcart/cart.html'

@login_required
def cartView(request):
    template_name = 'productcart/cart.html'
    username = request.user.username
    carts = Cart.objects.filter(user__username=username).order_by('-id')
    context={
        'carts':carts,
    }
    return render(request, template_name, context)

@login_required
def addcart(request,**kwargs):
    user = request.user
    p_name=kwargs['product'].capitalize()
    product = Product.objects.filter(p_name__iexact=p_name).first()
    print(p_name)
    print("product",user,product)
    try:
        cartexist = Cart.objects.filter(user__exact=user,product__exact=product).first()
        print(cartexist)
        if(user and product and not(cartexist)):
            Cart.objects.create(user=user,product=product)
            # return HttpResponse('success')
        else:
            print("failed")
    except:
        raise Http404("Failed to Create Cart or else Cart already exists")
    print("user = ",user,product)
    return redirect('cart')