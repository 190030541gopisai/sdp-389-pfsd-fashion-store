from django.urls import path

from . import views

urlpatterns = [
    path('',views.search,name="search-product" )

    # path('<str:query>',views.search_query,name="search-product" )
]