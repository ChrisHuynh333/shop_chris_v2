from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "shop/index.html")

def product(request, product):
    return render(request, "shop/products_individual.html", {
        "product": product
    })

def category(request, category):
    return render(request, "shop/products_by_category.html", {
        "category": category
    })

def all_products(request):
    return render(request, "shop/all_products.html")

def account(request):
    return render(request, "shop/account.html")

def login(request):
    return render(request, "shop/login.html")

def register(request):
    return render(request, "shop/register.html")

def cart(request):
    return render(request, "shop/cart.html")

def order_complete(request):
    return render(request, "shop/order_complete.html")