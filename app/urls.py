from django.urls import path
from app.views import *


urlpatterns = [
    path('', home, name='home'),
    path('aboutus', aboutus, name='aboutus'),
    path('event', event, name='event'),
    path('contact', contact, name="contact"),
    path('registeration', registeration, name='registeration'),
    path('login', login, name='login'),
    path('discovermore', discovermore, name='discovermore'),
    path('dashboard', dashboard, name='dashboard'),
    path('logout', logout, name='logout'),
    # path('store/', store, name='store'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('update_item/', updateItem, name='update_item'),
]