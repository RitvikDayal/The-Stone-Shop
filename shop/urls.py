from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tss/about/', views.about, name='about'),
    path('tss/contact-us/', views.contact, name='contact-us'),
    path('shop/', views.shop, name='shop'),
    path('tss/cart/', views.cart, name='cart'),
    path('tss/checkout/', views.checkout, name='checkout'),
    path('process_order/', views.processOrder, name='process_order'),
    path('update/', views.updateItem, name='update'),
]