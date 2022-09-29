from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# auth_views.

urlpatterns = [
     # path('signin/', views.signin, name='signin'),
     path('login/', auth_views.LoginView.as_view(template_name="register/login.html") , name='login'),
     path('logout/',auth_views.LogoutView.as_view(template_name="register/logout.html"),name="logout"),
     path('register/',views.register,name="register"),
]