from django.shortcuts import render

# Create your views here.

def home(request):
    logged_in = request.user.is_authenticated
    context = {'logged_in':logged_in,'title':'Home - RedStore', 'header':'header'}
    return render(request,'core/index.html', context)

def products(request):
    logged_in = request.user.is_authenticated
    context = {'logged_in':logged_in,'title': 'Products - RedStore', 'header':'header2'}
    return render(request,'core/products.html',context)

def product(request):
    logged_in = request.user.is_authenticated
    context = {'logged_in':logged_in,'title': 'Product - RedStore', 'header':'header2'}
    return render(request, 'core/product_details.html', context)

def cart(request):
    logged_in = request.user.is_authenticated
    context = {'logged_in':logged_in,'title': 'Cart - RedStore', 'header':'header2'}
    return render(request, 'core/cart.html', context)