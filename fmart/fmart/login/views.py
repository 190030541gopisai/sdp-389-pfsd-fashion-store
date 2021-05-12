from django.shortcuts import render,HttpResponse

# # Create your views here.
# def index(request):
#     return render(request,'Hi prands.html')


def base(request):
	template_name="base.html"
	return render(request, template_name)



def home(request):
    return render(request,'homepage.html')



# def register(request):
#     return render(request,'Registration.html')


def formals(request):
    return render(request,'Formals.html')
def payment(request):
    return render(request,'payment.html')
def sherwani(request):
    return render(request,'sherwani.html')
def tshirt(request):
    return render(request,'tshirt.html')
def about(request):
    return render(request,'about.html')
def kurtis(request):
    return render(request,'kurtis.html')
def saree(request):
    return render(request,'sarees.html')

