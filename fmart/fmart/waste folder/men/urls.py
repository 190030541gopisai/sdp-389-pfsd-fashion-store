from django.urls import path
from . import views
# from .views import (
#     MensProducts
# )

urlpatterns = [
 
    path('',views.menshome,name="mens"),
    # path('formals',views.formals,name="formals"),
    # path('tshirts',views.tshirts,name="tshirts"),
    # # path('<str:p_category>',MensProducts.as_view(template_name="men/mensproduct.html"),name="sherwani"),
    # #  path('sherwani',views.mensProducts,name="sherwani"),
    # path('sherwani',views.sherwani,name="sherwani"),

    # path('<str:p_type>/<str:p_category>/',MensProducts.as_view(template_name="men/mensproduct.html"),name="mens-product")
    path('<str:p_type>/<str:p_category>/',views.mensProduct,name="mens-product")

]