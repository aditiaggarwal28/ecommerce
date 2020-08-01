
from django.urls import path
from . import views


urlpatterns = [

    path('',views.index, name="shopindex"),
    path('about',views.about, name="shopabout"),
    path('contact',views.contact, name="shopcontact"),
    path('tracker',views.tracker, name="shoptracker"),
    path('products/<int:myid>',views.prodview, name="shopprodview"),
    path('search',views.search, name="shopsearch"),
    path('checkout',views.checkout, name="shopcheckout"),
    path('payment',views.payment, name="shoppayment")

]