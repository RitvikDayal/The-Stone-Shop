from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
import datetime

# local imports
from .models import *
from .utils import cartData

# Shop Home
def home(request):
    
    data = cartData(request)

    products = Product.objects.all() # all the products
    cartItems = data['cartItems'] # cart item count
    items = data['items'] # Items in Cart
    
    context = {
        'products': products,
        'cartItems': cartItems,
        'items': items,
    }
    return render(request, 'shop/index.html', context=context)

# Shop About :- /tss/about
def about(request):
    return render(request, 'shop/about.html')

# Shop ContactUs:- /tss/contact
def contact(request):
    return render(request, 'shop/contact-us.html')

# Shop Items :- /shop
def shop(request):
    products = Product.objects.all()
    data = cartData(request)
    cartItems = data['cartItems']
    items = data['items'] # Items in Cart
    
    context = {
        'products': products,
        'cartItems': cartItems,
        'items': items,
    }
    return render(request, 'shop/shop.html', context=context)

# Item Cart :- tss/cart/
def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {
        'items': items, # items in the cart
        'order': order, # order object for the customer
        'cartItems': cartItems, # cart item count
        'shipping':False, # shiiping boolean value to ask for address or not
    }
    return render(request, 'shop/cart.html', context=context)

@login_required
# Checkout tss/checkout
def checkout(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {
        'items': items,   # items in the cart 
        'order': order,   # order object for the customer
        'cartItems': cartItems,  # cart item count
        'shipping':False   # shiiping boolean value to ask for address or not
    }
    return render(request, 'shop/checkout.html', context=context)

# Item Detail
# def itemDetail(request):
#     return render(request, 'shop/item-detail.html')

# To update Items in the cart of the customer
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action: ', action)
    print('Product: ', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete = False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    orderItem.quantity+= 1 if action == 'add' else -1
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    
    return JsonResponse('Item was added', safe=False)

# Function to process Order
def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        # Creating Customer
        customer = request.user.customer
        customer.fname = data['user']['firstName']
        customer.lname = data['user']['lastName']
        customer.email = data['user']['email']

        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        total = float(data['user']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True

        order.save()

        if order.shipping == True:
            ShippingAdress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address']+' '+data['shipping']['address2'],
                city=data['shipping']['country'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zip'],
            )
    else:
        return redirect('login')

    return JsonResponse('Payment Complete', safe=False)
