from django.contrib import admin
from django.urls import path
from mainapp.views import *

urlpatterns = [
    path('',index,name='index'),
    path('events/',events,name='events'),
    path('flights/',flights,name='flights'),
    path('holidays/',holidays,name='holidays'),
    path('artwork/',artwork,name='artwork'),
    path('movies/',movies,name='movies'),
    path('books/',books,name='books'),
    path('music/',music,name='music'),
    path('login/',signin,name='login'),
    path('cart/',cart,name='cart'),
    path('signup/',signup,name='signup'),
    path('checkout/',checkout,name='checkout'),
    path('event-checkout/',event_checkout,name='event-checkout'),
    path('holidays-checkout/',holidays_checkout,name='holidays-checkout'),
    path('contact/',contact,name='contact')
    ]
