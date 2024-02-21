from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('product/', views.product, name='product'),
    path('cart/', views.cart, name='cart'),
    path('account/', views.account, name='account')
]