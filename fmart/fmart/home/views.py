from django.shortcuts import render

# Create your views here.

def home(request):
	template_name="home/index.html"

	
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
		},
		{	
			'name':'Kurtis',
			'image':'images/Kurtis.png',
			'price':'Rs.100',
			'description':'some text',
			'formaction':'Kurtis'
		},
		{	
			'name':'Sarees',
			'image':'images/Sarees.png',
			'price':'Rs.100',
			'description':'some text',
			'formaction':'Sarees'
		},
		{	
			'name':'Lehangachouli',
			'image':'images/Lehangachouli.png',
			'price':'Rs.100',
			'description':'some text',
			'formaction':'Lehangachouli'
		},
		

	]
	context={
		'categories':categories,
	}
	return render(request,template_name,context)