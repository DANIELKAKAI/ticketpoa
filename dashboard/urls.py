
from django.urls import path
from dashboard.views import *

urlpatterns = [
    path('', merchant,name='merchant'),
    path('account', merchant_account,name='merchant_account'),
    path('finance', merchantfinance,name='merchantfinance'),
    path('products', merchantproducts,name='merchantproducts'),
    path('profile', merchantprofile,name='merchantprofile'),
    path('stores', merchantstores,name='merchantstores'),
    path('users', merchantusers,name='merchantusers'),
    path('newstore', newstore,name='newstore'),
    path('orders', orders,name='orders'),

]

