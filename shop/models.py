from django.db import models
from django.contrib.auth.models import User
from django import forms

class Customer(models.Model):
    customer = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.customer.username
    
class Product(models.Model):
    tag_choices = (
        ('new', 'New'),
        ('hot', 'hot'),
        ('exclusive', 'Exclusive')
    )

    CHOICES = (
        ('crystal', 'Crystal'),
        ('statue', 'Stone Sculpture'),
        ('pebble', 'Pebble')
    )
    name = models.CharField(max_length=60)
    category = models.CharField(max_length=25, choices=CHOICES, default='Crystal')
    price = models.FloatField()
    description = models.TextField(null=True, blank=True )
    product_image = models.ImageField(default='default_product.jpg', upload_to='products')
    discounted_price = models.FloatField(default=0.0)
    tag = models.CharField(max_length=10, choices=tag_choices, null=True, blank=True)
    available = models.BooleanField(default=True, null=True, blank=True)
    digital = models.BooleanField(default=False, null=True, blank=False)

    def __str__(self):
        return self.name

class Order(models.Model):
    SHIPPING_CHOICES = (
        ('standard', 'Standard Shiping'),
        ('express', 'Express Delivery'),
        ('nextDay', 'Next Business day')
    )
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    shipping_type = forms.ChoiceField(choices=SHIPPING_CHOICES, widget=forms.RadioSelect())
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True) 


    # Code block for shipping logic if there are digital items that doesn't need shipping the forms disappears.

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

    def __str__(self):
        return str(self.id)
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
    
class ShippingAdress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=250, null=False)
    city = models.CharField(max_length=150, null=False)
    state = models.CharField(max_length=150, null=False)
    zipcode = models.CharField(max_length=50, null=False)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.address


    