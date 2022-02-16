from django.urls import path
from . import views

app_name = "shop"
urlpatterns = [
    path("", views.index, name="index"),
    path("product/<str:product>", views.product, name="product"),
    path("category/<str:category>", views.category, name="category"),
    path("all-products", views.all_products, name="all_products"),
    path("account", views.account, name="account"),
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("cart", views.cart, name="cart"),
    path("order-complete", views.order_complete, name="order_complete")
]