from django.urls import path
from . import views
from .views import (
    MenuView
)

urlpatterns = [
 
    path('',views.home,name="home-index"),
    path('profile/',views.profile,name="profile"),
    path('about/',views.MenuView.as_view(template_name="home/about.html"),name="about"),
    path('clients/',views.MenuView.as_view(template_name="home/clients.html"),name="clients"),
    path('contact/',views.MenuView.as_view(template_name="home/contact.html"),name="contact"),
]