from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView,DetailView,TemplateView
from .models import (
	Product
)

def producttype(request,p_type,p_category):
	template_name='product/producttype.html'
	# print(p_type,p_category)
	# p_type = p_type.capitalize()
	# p_category = p_category.capitalize()
	# print(p_type,p_category)
	products=Product.objects.filter(p_type__exact=p_type,p_category__exact=p_category)
	context={
		'products':products
	}
	return render(request, template_name, context)

def menshome(request):
	# sherwani=Products.objects.filter(p_category__iexact="sherwani")
	# tshirts=Products.objects.filter(p_category__iexact="tshirts")
	# formals=Products.objects.filter(p_category__iexact="formals")
	
	categories=[
		{	
			'name':'Sherwani',
			'image':'product/images/men/sherwani.png',
			# #'price':'Rs.100',
			# 'description':'some text',
		},
		{	
			'name':'Tshirts',
			'image':'product/images/men/t_shirts.png',
			# #'price':'Rs.100',
			# 'description':'some text',
		},
		{	
			'name':'Formals',
			'image':'product/images/men/formals.png',
			# #'price':'Rs.100',
			# 'description':'some text',
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
			'image':'product/images/women/Kurtis.png',
			#'price':'Rs.100',
			# 'description':'some text',
			# 'formaction':'kurtis'
		},
		{	
			'name':'Sarees',
			'image':'product/images/women/Sarees.png',
			#'price':'Rs.100',
			# 'description':'some text',
			# 'formaction':'sarees'
		},
		{	
			'name':'Lehangachouli',
			'image':'product/images/women/Lehangachouli.png',
			#'price':'Rs.100',
			# 'description':'some text',
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
			'name':'Traditional',
			'image':'product/images/kids/kidstraditional.png',
			# 'image':'images/kidstraditional.jpeg',
			#'price':'Rs.100',
			# 'description':'some text',
			# 'formaction':'kurtis'
		},
		{	
			'name':'Tshirts',
			'image':'product/images/kids/kidstshirts.jpg',
			#'price':'Rs.100',
			# 'description':'some text',
			# 'formaction':'sarees'
		},
		{	
			'name':'OneSies',
			'image':'product/images/kids/kidsonesies.png',
			#'price':'Rs.100',
			# 'description':'some text',
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

