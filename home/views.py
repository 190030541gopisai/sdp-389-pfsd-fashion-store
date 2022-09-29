from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
# Create your views here.

class MenuView(TemplateView):
	template_name = "home/about.html"


@login_required
def profile(request):
	template_name='home/profile.html'
	return render(request, template_name)

def home(request):
	template_name="home/index.html"

	# categories=[
	# 	{	
	# 		'name':'sherwani',
	# 		'image':'images/sherwani.png',
	# 		'price':'Rs.100',
	# 		'description':'some text',
	# 		'formaction':'sherwani'
	# 	},
	# 	{	
	# 		'name':'T-shirts',
	# 		'image':'images/img_1.png',
	# 		'price':'Rs.100',
	# 		'description':'some text',
	# 		'formaction':'T-shirts'
	# 	},
	# 	{	
	# 		'name':'Formals',
	# 		'image':'images/Formals.png',
	# 		'price':'Rs.100',
	# 		'description':'some text',
	# 		'formaction':'Formals'
	# 	},
	# 	{	
	# 		'name':'Kurtis',
	# 		'image':'images/Kurtis.png',
	# 		'price':'Rs.100',
	# 		'description':'some text',
	# 		'formaction':'Kurtis'
	# 	},
	# 	{	
	# 		'name':'Sarees',
	# 		'image':'images/Sarees.png',
	# 		'price':'Rs.100',
	# 		'description':'some text',
	# 		'formaction':'Sarees'
	# 	},
	# 	{	
	# 		'name':'Lehangachouli',
	# 		'image':'images/Lehangachouli.png',
	# 		'price':'Rs.100',
	# 		'description':'some text',
	# 		'formaction':'Lehangachouli'
	# 	},
		

	# ]
	# context={
	# 	'categories':categories,
	# }
	return render(request,template_name)