from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from payment.models import Payment
from .models import Orders
# Create your views here.


@login_required()
def orders(request):
    template_name = "orders/orders.html"
    user = request.user
    orders = Orders.objects.filter(payment__user__username__iexact=user.username)
    context={
        'orders':orders
    }
    return render(request, template_name, context)