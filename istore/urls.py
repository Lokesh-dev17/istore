from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('products',views.products,name="products"),
    path('feedback',views.feedback,name="feedback"),
    path('log_in',views.logIn,name="log_in"),
    path('sign_up',views.signup,name="sign_up"),
    path('log_out',views.logout,name="log_out"),
    path('sales-book',views.sales_book,name="sales-book"),
   
]
