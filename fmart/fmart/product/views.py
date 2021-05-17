from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView,DetailView,TemplateView
from home.models import (
	Product
)

# class ProductDetailView(DetailView):
# 	model = Product

def producttype(request,p_type,p_category):
	template_name='product/producttype.html'
	p_type = p_type.capitalize()
	p_category = p_category.capitalize()
	products=Product.objects.filter(p_type__exact=p_type,p_category__exact=p_category)
	context={
		'products':products
	}
	return render(request, template_name, context)

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
		},
		{	
			'name':'formals',
			'image':'images/Formals.png',
			'price':'Rs.100',
			'description':'some text',
		}
	]
	template_name="product/producthome.html"
	context={
		'categories':categories,
		'type':'Men',
		'formaction':'product-type'
	}
	return render(request,template_name,context)

def womenshome(request):
	categories=[
		{	
			'name':'Kurtis',
			'image':'images/Kurtis.png',
			'price':'Rs.100',
			'description':'some text',
			# 'formaction':'kurtis'
		},
		{	
			'name':'Sarees',
			'image':'images/Sarees.png',
			'price':'Rs.100',
			'description':'some text',
			# 'formaction':'sarees'
		},
		{	
			'name':'Lehangachouli',
			'image':'images/Lehangachouli.png',
			'price':'Rs.100',
			'description':'some text',
			# 'formaction':'lehangachouli'
		},
		

	]
	template_name="product/producthome.html"
	context={
		'categories':categories,
		'type':'Women',
		'formaction':'product-type'
	}
	return render(request,template_name,context)

def kidshome(request):
	categories=[
		{	
			'name':'Traditional wear',
			'image':'images/Kurtis.png',
			'price':'Rs.100',
			'description':'some text',
			# 'formaction':'kurtis'
		},
		{	
			'name':'Tshirts',
			'image':'images/Sarees.png',
			'price':'Rs.100',
			'description':'some text',
			# 'formaction':'sarees'
		},
		{	
			'name':'OneSies',
			'image':'images/Lehangachouli.png',
			'price':'Rs.100',
			'description':'some text',
			# 'formaction':'lehangachouli'
		},
		

	]
	template_name="product/producthome.html"
	context={
		'categories':categories,
		'type':'Kids',
		'formaction':'product-type'
	}
	return render(request,template_name,context)

