from django.shortcuts import render

# Create your views here.

def home(request):
    context = {'title':'Home - RedStore', 'header':'header'}
    return render(request,'core/index.html', context)

def products(request):
    context = {'title': 'Products - RedStore', 'header':'header2'}
    return render(request,'core/products.html',context)

def product(request):
    context = {'title': 'Product - RedStore', 'header':'header2'}
    return render(request, 'core/product_details.html', context)