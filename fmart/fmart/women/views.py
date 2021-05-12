from django.shortcuts import render

# Create your views here.


def womenshome(request):
	categories=[
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
	template_name="women/womens.html"
	context={
		'categories':categories,
	}
	return render(request,template_name,context)