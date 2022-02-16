from django.shortcuts import render
from shop.models import *
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "shop/index.html")

def product(request, product):
    return render(request, "shop/products_individual.html", {
        "product": product
    })

def category(request, category):
    products = Product.objects.all().order_by('name')
    product_list_for_cat = []
    for product in products:
        if str(product.category) == category:
            product_list_for_cat.append(product)
    print(product_list_for_cat)
    return render(request, "shop/products_by_category.html", {
        "category": category,
        "products": product_list_for_cat
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