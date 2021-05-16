from django.urls import path
from . import views

urlpatterns = [
 
    path('',views.womenshome,name="womens"),
    # path('kurtis',views.kurtis,name="kurtis"),
    # path('sarees',views.sarees,name="sarees"),
    # path('lehangachouli',views.lehangachouli,name="lehangachouli"),
]