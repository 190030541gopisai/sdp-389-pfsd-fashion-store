from django.urls import path
from . import views
urlpatterns = [
    path('menshome',views.menshome,name="mens-home"),
    path('womenshome',views.womenshome,name="womens-home"),
    path('kidshome',views.kidshome,name="kids-home"),
    path('<str:p_type>/<str:p_category>/',views.producttype,name="product-type")
]