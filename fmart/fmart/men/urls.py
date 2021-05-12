from django.urls import path
from . import views

urlpatterns = [
 
    path('',views.menshome,name="mens"),
    
]