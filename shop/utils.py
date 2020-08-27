import json
from .models import *

def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}

    items = []
    order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping':False}
    cartItems = order['get_cart_items']

    for i in cart:
        try:
            cartItems += cart[i]['quantity']
            product = Product.objects.get(id=i)
            total = (product.price * cart[i]['quantity'])
            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]['quantity']
            
            # Creating Item
            item = {
                'product':{
                    'id': product.id,
                    'name': product.name,
                    'price':product.price,
                    'imageURL':product.product_image.url,
                },
                'quantity': cart[i]['quantity'],
                'get_total':total,
            }

            items.append(item)#adding created item to cart item list

            if product.digital == False:
                order['shipping'] = True
        except:
            pass

    return {
        'cartItems':cartItems,
        'order':order,
        'items':items
    }

def cartData(request):
    cookieData = cookieCart(request)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        if order.get_cart_items == 0:
            order = cookieData['order']
            cartItems = cookieData['cartItems']
            items = cookieData['items']
        else:
            cartItems = order.get_cart_items
            items = order.orderitem_set.all()
    else:
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']

    return {
            'cartItems':cartItems,
            'order':order,
            'items':items
        }