from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView,DetailView,TemplateView
from home.models import (
	Product
)


def mensProduct(request,p_type,p_category):
	template_name='men/mensproduct.html'
	p_type = p_type.capitalize()
	p_category = p_category.capitalize()
	# print(p_type,p_category)
	products=Product.objects.filter(p_type__exact=p_type,p_category__exact=p_category)
	# print("products",products)
	context={
		'products':products
	}
	return render(request, template_name, context)


# class MensProducts(TemplateView):
# 	template_name='men/mensproduct.html'
# 	def get_context_data(self,*args, **kwargs):
# 		context = super(MensProducts, self).get_context_data(*args,**kwargs)
# 		print('kewargs',kwargs)
# 		p_type=kwargs['p_type']
# 		p_category=kwargs['p_category']
# 		print(p_type,p_category)
# 		# context['products'] = Product.objects.filter(p_type__exact=p_type,p_category__exact=p_category)
# 		# return context
# 		extra_context={'products':Product.objects.filter(p_type__exact=p_type,p_category__exact=p_category)}
# 		# context['users'] = YourModel.objects.all()
		# return context
	# def get_context_data(self, **kwargs):
	# 	context = super().get_context_data(**kwargs)
	# 	print('kewargs',kwargs)
	# 	p_type=kwargs['p_type']
	# 	p_category=kwargs['p_category']
	# 	context['products'] = Product.objects.filter(p_type__exact=p_type,p_category__exact=p_category)
	# 	return context

# def formals(request):
# 	template_name="men/mensproduct.html"
# 	p_type='Men'
# 	p_category='Formals'
# 	products=Product.objects.filter(p_type__exact=p_type,p_category__exact=p_category)

# 	context = {
# 		'products':products
# 	}
# 	return render(request, template_name,context)

# def tshirts(request):
# 	template_name="men/mensproduct.html"
# 	p_type='Men'
# 	p_category='Tshirts'
# 	products=Product.objects.filter(p_type__exact=p_type,p_category__exact=p_category)

# 	context = {
# 		'products':products
# 	}
# 	return render(request, template_name,context)

# def sherwani(request):
# 	template_name="men/mensproduct.html"
# 	p_type='Men'
# 	p_category='Sherwani'
# 	products=Product.objects.filter(p_type__exact=p_type,p_category__exact=p_category)
# 	context = {
# 		'products':products
# 	}
# 	return render(request, template_name,context)


def menshome(request):

	categories=[
		{	
			'name':'sherwani',
			'image':'images/sherwani.png',
			'price':'Rs.100',
			'description':'some text',
			

		},
		{	
			'name':'tshirts',
			'image':'images/img_1.png',
			'price':'Rs.100',
			'description':'some text',
			# 'formaction':'tshirts'
			
		},
		{	
			'name':'formals',
			'image':'images/Formals.png',
			'price':'Rs.100',
			'description':'some text',
			# 'formaction':'formals'
			
		}
	]
	template_name="men/mens.html"
	context={
		'categories':categories,
		'type':'Men',
		'formaction':'mens-product'

	}
	return render(request,template_name,context)

