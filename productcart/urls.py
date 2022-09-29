from django.urls import path
from . import views

urlpatterns = [
 
    path('',views.cartView,name="cart"),
    path('addcart/<str:user>/<str:product>',views.addcart,name="addcart"),
    path('delete/<int:pk>',views.DeleteCartView.as_view(),name="delete-cart")
]