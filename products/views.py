from django.shortcuts import render,get_object_or_404, redirect
from .models import Product
from decimal import Decimal


def product_list(request):
    products = Product.objects.all()

    return render(request, "shop.html", {
        'products':products
    })


def product_detail(request,slug):
    product = get_object_or_404(Product, slug=slug)

    return render(request, 'product_detail.html', {
        "product": product
    })
def add_to_cart(request,product_id):

    cart = request.session.get('cart', {}) 

    product_id = str(product_id)
    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1

    request.session['cart'] = cart


    return redirect('cart')

def cart(request):
    cart = request.session.get('cart', {})

    products = Product.objects.filter(
        id__in=cart.keys()
    )
    items = []
    subtotal = 0

    for product in products:
        quantity = cart[str(product.id)]
        item_total = product.price * quantity

        items.append({
            'product': product,
            'quantity': quantity,
            'item_total': item_total,
        })

        subtotal += item_total

        shipping = Decimal('15000.00') if items else Decimal('0.00')

        total = subtotal + shipping

    return render(request, 'cart.html', {
        'items': items,
        'subtotal': subtotal,
        'shipping': shipping,
        'total': total,
    })

def decrease_cart(request, product_id):
    cart_items = request.session.get('cart', {})
    product_id = str(product_id)

    if product_id in cart_items:
        cart_items[product_id] -= 1

        if cart_items[product_id] <= 0:
            del cart_items[product_id]

    request.session['cart'] = cart_items
    request.session.modified = True

    return redirect('cart')


def remove_from_cart(request, product_id):
    cart_items = request.session.get('cart', {})
    product_id = str(product_id)

    if product_id in cart_items:
        del cart_items[product_id]

    request.session['cart'] = cart_items
    request.session.modified = True

    return redirect('cart')

