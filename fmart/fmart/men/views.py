from django.shortcuts import render

# Create your views here.


def menshome(request):
	categories=[
		{	
			'name':'sherwani',
			'image':'images/sherwani.png',
			'price':'Rs.100',
			'description':'some text',
			'formaction':'sherwani'
		},
		{	
			'name':'T-shirts',
			'image':'images/product_02.jpg',
			'price':'Rs.100',
			'description':'some text',
			'formaction':'T-shirts'
		},
		{	
			'name':'Formals',
			'image':'images/Formals.png',
			'price':'Rs.100',
			'description':'some text',
			'formaction':'Formals'
		}
	]
	template_name="men/mens.html"
	context={
		'categories':categories,
	}
	return render(request,template_name,context)