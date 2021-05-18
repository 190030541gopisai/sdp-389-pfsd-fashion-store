from django.urls import path
from . import views
urlpatterns = [
    # path('',views.payment,name="payment")
    
    
    # path('',views.PaymentView.as_view(),name="payment")
    path('<int:pk>',views.payment,name="payment"),

]