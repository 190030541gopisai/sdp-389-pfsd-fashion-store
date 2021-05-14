from django.urls import path
from . import views

urlpatterns = [
 
    path('',views.menshome,name="mens"),
    path('formals',views.formals,name="formals"),
    path('tshirts',views.tshirts,name="tshirts"),
    path('sherwani',views.sherwani,name="sherwani"),
]