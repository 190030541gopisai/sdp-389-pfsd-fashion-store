from django.shortcuts import render

# Create your views here.
# def kurtis(request):
# 	template_name="women/kurtis.html"
# 	return render(request, template_name)

# def sarees(request):
# 	template_name="women/sarees.html"
# 	return render(request, template_name)

# def lehangachouli(request):
# 	template_name="women/lehangachouli.html"
# 	return render(request, template_name)

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
	template_name="men/mens.html"
	context={
		'categories':categories,
		'type':'Women',
		'formaction':'mens-product'
	}
	return render(request,template_name,context)