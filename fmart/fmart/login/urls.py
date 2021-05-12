from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    # path('register/',views.register,name="register"),


    path('base/',views.base,name="base"),

    path('home/',views.home,name="home"),

    path('formals/',views.formals,name="formals"),
    path('payment/',views.payment,name="payment"),
    path('sherwani/',views.sherwani,name="sherwani"),
    path('tshirt/',views.tshirt,name="tshirt"),
    path('about/',views.about,name="about"),
    path('kurtis/',views.kurtis,name="kurtis"),
    path('sarees/',views.saree,name="sarees"),


    
]