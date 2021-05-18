from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm

from django.contrib import messages


# Create your views here.

# def signin(request):
#     form=10
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username=form.cleaned_data.get('username')
#             messages.success(request, 'Account created for {}!'.format(username))
#             return redirect('home-index')
#     else:
#         form = UserCreationForm()
#     return render(request,'register/signin.html',{'form':form})



def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, 'Account created for {}! please log in'.format(username))
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'register/registration.html',{'form':form})


