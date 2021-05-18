from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import PaymentForm,CardForm,AddressForm

from django.views.generic import TemplateView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from home.models import Product

class PaymentView(LoginRequiredMixin,DetailView):
    template_name = "payment/payment.html"
    model = Product
    def get_context_data(self, **kwargs):
        # context = super(PaymentTemplateView,self).get_context_data(**kwa)
        context = super(PaymentView, self).get_context_data(**kwargs) 
        if self.request.method == 'POST':
            form1 = AddressForm(request.POST)
            form2 = CardForm(request.POST)
            # print("formdetails",form1,form2,sep='\n')
            # if form1.is_valid() and form2.is_valid():
            #     form1.save() 
            #     form2.save()
        else:
            form1 = AddressForm()
            form2 = CardForm()
        context['form1']=form1
        context['form2']=form2
        print("okokok")
        return context
    # def form_valid(self, form):
    #     form.save()
    #     super().form_valid(form)


# class PaymentView(TemplateView):
#     template_name = "payment/payment.html"

#     def get_context_data(self, **kwargs):
#         # context = super(PaymentTemplateView,self).get_context_data(**kwa)
#         context = super(PaymentView, self).get_context_data(**kwargs) 
#         if self.request.method == 'POST':
#             form1 = AddressForm(request.POST)
#             form2 = CardForm(request.POST)
#         else:
#             form1 = AddressForm()
#             form2 = CardForm()
#         context['form1']=form1
#         context['form2']=form2
#         print("okokok")
#         return context
#     # def form_valid(self, form):
#     #     form.instance.



@login_required
def payment(request,pk):
    template_name = "payment/payment.html"
    product = Product.objects.filter(pk__exact=pk).first()
    print(product)
    if request.method=='POST':
        form1 = AddressForm(request.POST)
        form2 = CardForm(request.POST)
    else:
        form1 = AddressForm()
        form2 = CardForm()
    context = {
        'form1':form1,
        'form2':form2,
        'object':product, 
    }
    return render(request, template_name,context)
    

