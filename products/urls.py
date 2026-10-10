from django.urls import path
from .views import (
    product_list,
    product_detail,
    add_to_cart,
    cart,
    decrease_cart,
    remove_from_cart,
)

urlpatterns = [
    path('', product_list, name='product_list'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name = "add_to_cart"),
    path('decrease-cart/<int:product_id>/', decrease_cart, name='decrease_cart'),
    path('remove-from-cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/', cart, name = 'cart'),
    path('<slug:slug>/', product_detail, name="product_detail"),
]