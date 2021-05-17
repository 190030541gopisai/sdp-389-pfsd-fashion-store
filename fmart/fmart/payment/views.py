from django.shortcuts import render

# Create your views here.
def payment(request):
    template_name = "payment/payment.html"
    return render(request, template_name)
    

