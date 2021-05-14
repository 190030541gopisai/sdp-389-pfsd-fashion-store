from django.shortcuts import render

# Create your views here.
def formals(request):
	template_name="men/formals.html"
	return render(request, template_name)

def tshirts(request):
	template_name="men/tshirts.html"
	return render(request, template_name)

def sherwani(request):
	template_name="men/sherwani.html"
	return render(request, template_name)

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
			'image':'images/img_1.png',
			'price':'Rs.100',
			'description':'some text',
			'formaction':'tshirts'
		},
		{	
			'name':'Formals',
			'image':'images/Formals.png',
			'price':'Rs.100',
			'description':'some text',
			'formaction':'formals'
		}
	]
	template_name="men/mens.html"
	context={
		'categories':categories,
	}
	return render(request,template_name,context)

